from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.ip_family_enum import IPFamilyEnum, check_ip_family_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_address_list_active_condition_instances_item import IPAddressListActiveConditionInstancesItem
    from ..models.ip_address_list_created import IPAddressListCreated
    from ..models.ip_address_list_organization_type_0 import IPAddressListOrganizationType0
    from ..models.ip_address_list_prefix import IPAddressListPrefix
    from ..models.ip_address_list_workspace_type_0 import IPAddressListWorkspaceType0


T = TypeVar("T", bound="IPAddressList")


@_attrs_define
class IPAddressList:
    """Lightweight serializer for IPAddress list views.
    Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectListSerializer.
    organization/workspace automatisch von ManagedObjectListSerializer.

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            labels (Any):
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[IPAddressListActiveConditionInstancesItem]):
            organization (IPAddressListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (IPAddressListWorkspaceType0 | None):
            created (IPAddressListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            prefix (IPAddressListPrefix):
            kind (IPFamilyEnum | Unset): * `ipv4` - IPv4
                * `ipv6` - IPv6
            ip_address (None | str | Unset): The actual IP address (e.g., 192.168.1.10 or 2001:db8::1)
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[IPAddressListActiveConditionInstancesItem]
    organization: IPAddressListOrganizationType0 | None
    organization_priority: bool
    workspace: IPAddressListWorkspaceType0 | None
    created: IPAddressListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    prefix: IPAddressListPrefix
    kind: IPFamilyEnum | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_address_list_organization_type_0 import IPAddressListOrganizationType0  # noqa: PLC0415
        from ..models.ip_address_list_workspace_type_0 import IPAddressListWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, IPAddressListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, IPAddressListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        prefix = self.prefix.to_dict()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "prefix": prefix,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_list_active_condition_instances_item import (
            IPAddressListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.ip_address_list_created import IPAddressListCreated  # noqa: PLC0415
        from ..models.ip_address_list_organization_type_0 import IPAddressListOrganizationType0  # noqa: PLC0415
        from ..models.ip_address_list_prefix import IPAddressListPrefix  # noqa: PLC0415
        from ..models.ip_address_list_workspace_type_0 import IPAddressListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = IPAddressListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> IPAddressListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = IPAddressListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAddressListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> IPAddressListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = IPAddressListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAddressListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = IPAddressListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        prefix = IPAddressListPrefix.from_dict(d.pop("prefix"))

        _kind = d.pop("kind", UNSET)
        kind: IPFamilyEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_ip_family_enum(_kind)

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ip_address", UNSET))

        ip_address_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            prefix=prefix,
            kind=kind,
            ip_address=ip_address,
        )

        ip_address_list.additional_properties = d
        return ip_address_list

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
