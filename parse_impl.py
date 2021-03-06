#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.reg import Registry
from models.permissions import Role
from storage.impl.deserialize import Deserializer
from storage.schema.deserialize import SchemaDeserializer
from pprint import pprint
import json


if __name__ == '__main__':
    impl_reg = Registry()
    resource_reg = Registry()
    type_reg = Registry()

    impl_deserializer = Deserializer('./schema/implementation')
    spec_deserializer = SchemaDeserializer('./schema')

    for resource_name in impl_deserializer.resources():
        impl_reg.add_type(impl_deserializer.decode_resource(resource_name))

    for type_name in spec_deserializer.types():
        type_reg.add_type(spec_deserializer.decode_type(type_name))

    for resource_name in spec_deserializer.resources():
        resource_reg.add_type(spec_deserializer.decode_resource(resource_name))

    spec_resource_names = set(resource_reg.types.keys())
    impl_resource_names = set(impl_reg.types.keys())
    print "\n>>> Unimplemented Resources:"
    pprint(spec_resource_names.difference(impl_resource_names))
    print "\n>>> Unspecified Resources:"
    pprint(impl_resource_names.difference(spec_resource_names))

    spec_methods = []
    spec_fields = {}
    impl_methods = []
    impl_fields = {}
    permissions = {}
    methods = {}
    for rn in spec_resource_names.intersection(impl_resource_names):
        spec_resource = resource_reg.get_type(rn)
        for mn in spec_resource.methods:
            fmn = rn + '.' + mn
            spec_methods.append(fmn)

        impl_resource = impl_reg.get_type(rn)
        for mn in impl_resource.methods:
            fmn = rn + '.' + mn
            impl_methods.append(fmn)

        for mn in set(spec_resource.methods).intersection(set(impl_resource.methods)):
            spec_method = spec_resource.get_method(mn)
            for fn in spec_method.fields:
                spec_fields[rn + '.' + mn + '.' + fn] = spec_method.get_field(fn)

            impl_method = impl_resource.get_method(mn)
            for fn in impl_method.fields:
                impl_fields[rn + '.' + mn + '.' + fn] = impl_method.get_field(fn)

            permissions[rn + '.' + mn] = {}
            permissions[rn + '.' + mn]['spec'] = spec_method.permissions
            permissions[rn + '.' + mn]['impl'] = impl_method.permissions

    print "\n>>> Unimplemented methods:"
    pprint(set(spec_methods).difference(set(impl_methods)))
    print "\n>>> Unspecified methods:"
    pprint(set(impl_methods).difference(set(spec_methods)))

    print "\n>>> Unimplemented fields:"
    for field in set(spec_fields.keys()).difference(set(impl_fields.keys())):
        print field.split(u'.')[0] + ',' + field.split(u'.')[1] + u',' + field.split(u'.')[2]
    print "\n>>> Unspecified fields:"
    for field in set(impl_fields.keys()).difference(set(spec_fields.keys())):
        print field.split(u'.')[0] + ',' + field.split(u'.')[1] + u',' + field.split(u'.')[2]

    print "\n>>> Incorrect field type:"
    for fn in set(spec_fields.keys()).intersection(set(impl_fields.keys())):
        if spec_fields[fn].datatypename != impl_fields[fn].datatypename:
            print fn + ',' + spec_fields[fn].datatypename + ',' + impl_fields[fn].datatypename

    print "\n>>> Incorrect requirement modifier:"
    for fn in set(spec_fields.keys()).intersection(set(impl_fields.keys())):
        if spec_fields[fn].required != impl_fields[fn].required:
            print fn + ',' + str(spec_fields[fn].required) + ',' + str(impl_fields[fn].required)

    print "\n>>> Methods:"
    for rn in spec_resource_names.union(impl_resource_names):
        if rn in resource_reg.types:
            spec_resource = resource_reg.get_type(rn)
            for mn in spec_resource.methods:
                fmn = rn + '.' + mn
                if fmn.lower() in methods:
                    methods[fmn.lower()][u'spec'] = True
                    methods[fmn.lower()][u'deprecated'] = spec_resource.get_method(mn).deprecated
                else:
                    methods[fmn.lower()] = {
                        u'name': fmn,
                        u'spec': True,
                        u'impl': False,
                        u'used': False,
                        u'deprecated': spec_resource.get_method(mn).deprecated,
                        u'private': False
                    }

        if rn in impl_reg.types:
            impl_resource = impl_reg.get_type(rn)
            for mn in impl_resource.methods:
                fmn = rn + '.' + mn
                if fmn.lower() in methods:
                    methods[fmn.lower()][u'impl'] = True
                    methods[fmn.lower()][u'private'] = impl_resource.get_method(mn).is_private
                else:
                    methods[fmn.lower()] = {
                        u'name': fmn,
                        u'spec': False,
                        u'impl': True,
                        u'used': False,
                        u'deprecated': False,
                        u'private': impl_resource.get_method(mn).is_private
                    }

    methods_usage = []
    with open('./schema/operation/usage.json') as f:
        data = json.load(f)
        methods_usage = []
        for m in data:
            methods_usage.append(m)

    for method in methods_usage:
        if method.lower() in methods:
            methods[method.lower()][u'used'] = True
        else:
            methods[method.lower()] = {
                u'name': method,
                u'spec': False,
                u'impl': False,
                u'used': True,
                u'deprecated': False,
                u'private': False
            }
    for full_method_name in methods:
        method = methods[full_method_name]

        resource = None
        method_name = None
        if len(method[u'name'].split(u'.')) > 0:
            resource = method[u'name'].split(u'.')[0]
        if len(method[u'name'].split(u'.')) > 1:
            method_name = method[u'name'].split(u'.')[1]

        print unicode(resource) + u',' +\
            unicode(method_name) + u',' +\
            unicode(method[u'spec']) + u',' +\
            unicode(method[u'impl']) + u',' +\
            unicode(method[u'used']) + u',' +\
            unicode(method[u'deprecated']) + u',' +\
            unicode(method[u'private'])

    print "\n>>> Permissions:"
    not_spec = []
    not_impl = []
    difference = []
    for mn in permissions:
        for role in Role.ROLES:
            if role not in permissions[mn]['spec']:
                not_spec.append((mn, role))
            if role not in permissions[mn]['impl']:
                not_impl.append((mn, role))
            if (role in permissions[mn]['spec'] and
                    role in permissions[mn]['impl']):
                spec_role = permissions[mn]['spec'][role]
                impl_role = permissions[mn]['impl'][role]
                if spec_role.access != impl_role.access:
                    difference.append((mn, role, spec_role.access, impl_role.access))

    print "\n>>>> Not Specified Permissions:"
    for (mn, role) in not_spec:
        print mn + ',' + role

    print "\n>>>> Not Implemented Permissions:"
    for (mn, role) in not_impl:
        print mn + ',' + role

    print "\n>>>> Difference in Permissions:"
    for (mn, role, sa, ia) in difference:
        print mn + ',' + role + ',' + unicode(sa) + ',' + unicode(ia)
