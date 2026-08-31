from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum

T = TypeVar("T", bound="OrganizationSimple")


@_attrs_define
class OrganizationSimple:
    """Simple Organization serializer for nested representations.

    Includes `url` field for direct navigation.

        Attributes:
            id (UUID):
            name (str):
            display_name (None | str): The display name is used to display the object in the UI. It can be different from
                the name.
            slug (None | str):
            reconciliation_running (bool):
            kind (GenericObjectKindEnum): * `generic` - Generic
            legal_name (str):
            tenant_id (None | str): 3-8 digit numeric tenant identifier
            support_pin (None | str): 8-digit numeric PIN for support authentication
            priority (bool): High priority organization flag
            url (str):
            upstream_organization_id (None | str): ID of the external system object managing this organization
            upstream_system_id (None | str): Identifier of the external system managing this organization
            keycloak_org_id (None | str):
    """

    id: UUID
    name: str
    display_name: None | str
    slug: None | str
    reconciliation_running: bool
    kind: GenericObjectKindEnum
    legal_name: str
    tenant_id: None | str
    support_pin: None | str
    priority: bool
    url: str
    upstream_organization_id: None | str
    upstream_system_id: None | str
    keycloak_org_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name: None | str
        display_name = self.display_name

        slug: None | str
        slug = self.slug

        reconciliation_running = self.reconciliation_running

        kind: str = self.kind

        legal_name = self.legal_name

        tenant_id: None | str
        tenant_id = self.tenant_id

        support_pin: None | str
        support_pin = self.support_pin

        priority = self.priority

        url = self.url

        upstream_organization_id: None | str
        upstream_organization_id = self.upstream_organization_id

        upstream_system_id: None | str
        upstream_system_id = self.upstream_system_id

        keycloak_org_id: None | str
        keycloak_org_id = self.keycloak_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "slug": slug,
                "reconciliation_running": reconciliation_running,
                "kind": kind,
                "legal_name": legal_name,
                "tenant_id": tenant_id,
                "support_pin": support_pin,
                "priority": priority,
                "url": url,
                "upstream_organization_id": upstream_organization_id,
                "upstream_system_id": upstream_system_id,
                "keycloak_org_id": keycloak_org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))

        reconciliation_running = d.pop("reconciliation_running")

        kind = check_generic_object_kind_enum(d.pop("kind"))

        legal_name = d.pop("legal_name")

        def _parse_tenant_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id"))

        def _parse_support_pin(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        support_pin = _parse_support_pin(d.pop("support_pin"))

        priority = d.pop("priority")

        url = d.pop("url")

        def _parse_upstream_organization_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upstream_organization_id = _parse_upstream_organization_id(d.pop("upstream_organization_id"))

        def _parse_upstream_system_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        upstream_system_id = _parse_upstream_system_id(d.pop("upstream_system_id"))

        def _parse_keycloak_org_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keycloak_org_id = _parse_keycloak_org_id(d.pop("keycloak_org_id"))

        organization_simple = cls(
            id=id,
            name=name,
            display_name=display_name,
            slug=slug,
            reconciliation_running=reconciliation_running,
            kind=kind,
            legal_name=legal_name,
            tenant_id=tenant_id,
            support_pin=support_pin,
            priority=priority,
            url=url,
            upstream_organization_id=upstream_organization_id,
            upstream_system_id=upstream_system_id,
            keycloak_org_id=keycloak_org_id,
        )

        organization_simple.additional_properties = d
        return organization_simple

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
