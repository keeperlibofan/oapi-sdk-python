# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import Callable

from ....config import Config
from ....context import Context
from ....event.event import set_event_callback

from .model import *


class DepartmentCreatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, DepartmentCreatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, DepartmentCreatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, DepartmentCreatedEvent], Any]) -> None
        handler = DepartmentCreatedEventHandler(callback)
        set_event_callback(conf, "contact.department.created_v3",
                          handler.handle, clazz=DepartmentCreatedEvent)


class DepartmentDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, DepartmentDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, DepartmentDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, DepartmentDeletedEvent], Any]) -> None
        handler = DepartmentDeletedEventHandler(callback)
        set_event_callback(conf, "contact.department.deleted_v3",
                          handler.handle, clazz=DepartmentDeletedEvent)


class DepartmentUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, DepartmentUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, DepartmentUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, DepartmentUpdatedEvent], Any]) -> None
        handler = DepartmentUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.department.updated_v3",
                          handler.handle, clazz=DepartmentUpdatedEvent)


class UserCreatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserCreatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserCreatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserCreatedEvent], Any]) -> None
        handler = UserCreatedEventHandler(callback)
        set_event_callback(conf, "contact.user.created_v3",
                          handler.handle, clazz=UserCreatedEvent)


class UserDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserDeletedEvent], Any]) -> None
        handler = UserDeletedEventHandler(callback)
        set_event_callback(conf, "contact.user.deleted_v3",
                          handler.handle, clazz=UserDeletedEvent)


class UserUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserUpdatedEvent], Any]) -> None
        handler = UserUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.user.updated_v3",
                          handler.handle, clazz=UserUpdatedEvent)


class UserGroupCreatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserGroupCreatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserGroupCreatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserGroupCreatedEvent], Any]) -> None
        handler = UserGroupCreatedEventHandler(callback)
        set_event_callback(conf, "contact.user_group.created_v3",
                          handler.handle, clazz=UserGroupCreatedEvent)


class UserGroupDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserGroupDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserGroupDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserGroupDeletedEvent], Any]) -> None
        handler = UserGroupDeletedEventHandler(callback)
        set_event_callback(conf, "contact.user_group.deleted_v3",
                          handler.handle, clazz=UserGroupDeletedEvent)


class UserGroupUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserGroupUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserGroupUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserGroupUpdatedEvent], Any]) -> None
        handler = UserGroupUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.user_group.updated_v3",
                          handler.handle, clazz=UserGroupUpdatedEvent)


class ScopeUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, ScopeUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, ScopeUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, ScopeUpdatedEvent], Any]) -> None
        handler = ScopeUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.scope.updated_v3",
                          handler.handle, clazz=ScopeUpdatedEvent)


class UserGroupMemberChangedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, UserGroupMemberChangedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, UserGroupMemberChangedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, UserGroupMemberChangedEvent], Any]) -> None
        handler = UserGroupMemberChangedEventHandler(callback)
        set_event_callback(conf, "contact.user_group.member.changed_v3",
                          handler.handle, clazz=UserGroupMemberChangedEvent)


class CustomAttrEventUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, CustomAttrEventUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, CustomAttrEventUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, CustomAttrEventUpdatedEvent], Any]) -> None
        handler = CustomAttrEventUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.custom_attr_event.updated_v3",
                          handler.handle, clazz=CustomAttrEventUpdatedEvent)


class EmployeeTypeEnumActivedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, EmployeeTypeEnumActivedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, EmployeeTypeEnumActivedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, EmployeeTypeEnumActivedEvent], Any]) -> None
        handler = EmployeeTypeEnumActivedEventHandler(callback)
        set_event_callback(conf, "contact.employee_type_enum.actived_v3",
                          handler.handle, clazz=EmployeeTypeEnumActivedEvent)


class EmployeeTypeEnumCreatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, EmployeeTypeEnumCreatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, EmployeeTypeEnumCreatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, EmployeeTypeEnumCreatedEvent], Any]) -> None
        handler = EmployeeTypeEnumCreatedEventHandler(callback)
        set_event_callback(conf, "contact.employee_type_enum.created_v3",
                          handler.handle, clazz=EmployeeTypeEnumCreatedEvent)


class EmployeeTypeEnumDeactivatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, EmployeeTypeEnumDeactivatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, EmployeeTypeEnumDeactivatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, EmployeeTypeEnumDeactivatedEvent], Any]) -> None
        handler = EmployeeTypeEnumDeactivatedEventHandler(callback)
        set_event_callback(conf, "contact.employee_type_enum.deactivated_v3",
                          handler.handle, clazz=EmployeeTypeEnumDeactivatedEvent)


class EmployeeTypeEnumDeletedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, EmployeeTypeEnumDeletedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, EmployeeTypeEnumDeletedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, EmployeeTypeEnumDeletedEvent], Any]) -> None
        handler = EmployeeTypeEnumDeletedEventHandler(callback)
        set_event_callback(conf, "contact.employee_type_enum.deleted_v3",
                          handler.handle, clazz=EmployeeTypeEnumDeletedEvent)


class EmployeeTypeEnumUpdatedEventHandler(object):
    def __init__(self, callback):
        # type: (Callable[[Context, Config, EmployeeTypeEnumUpdatedEvent], Any]) -> None
        self.handler = callback

    def handle(self, ctx, conf, event):  # type: (Context, Config, EmployeeTypeEnumUpdatedEvent) -> Any
        return self.handler(ctx, conf, event)

    @staticmethod
    def set_callback(conf, callback):
        # type: (Config, Callable[[Context, Config, EmployeeTypeEnumUpdatedEvent], Any]) -> None
        handler = EmployeeTypeEnumUpdatedEventHandler(callback)
        set_event_callback(conf, "contact.employee_type_enum.updated_v3",
                          handler.handle, clazz=EmployeeTypeEnumUpdatedEvent)
