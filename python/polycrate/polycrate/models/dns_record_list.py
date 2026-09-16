from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_record_type_enum import DNSRecordTypeEnum, check_dns_record_type_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_record_list_active_condition_instances_item import DNSRecordListActiveConditionInstancesItem
    from ..models.dns_record_list_created import DNSRecordListCreated
    from ..models.dns_record_list_organization_type_0 import DNSRecordListOrganizationType0
    from ..models.dns_record_list_workspace_type_0 import DNSRecordListWorkspaceType0
    from ..models.dns_zone_simple import DNSZoneSimple


T = TypeVar("T", bound="DNSRecordList")


@_attrs_define
class DNSRecordList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

        Attributes:
            id (str): Record identifier. Internal zones: UUID of the DNSRecord DB row. External zones: opaque composite
                '<zone_uuid>::<provider_assigned_id>' as returned by the list endpoint. Do not treat this field as UUID-only.
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
            active_condition_instances (list[DNSRecordListActiveConditionInstancesItem]):
            organization (DNSRecordListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (DNSRecordListWorkspaceType0 | None):
            created (DNSRecordListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            dns_zone (DNSZoneSimple):
            content (str): Record content: IP address, hostname, TXT string, …
            type_ (DNSRecordTypeEnum | Unset): * `A` - A
                * `AAAA` - AAAA
                * `CNAME` - CNAME
                * `MX` - MX
                * `TXT` - TXT
                * `SRV` - SRV
                * `CAA` - CAA
                * `NS` - NS
                * `PTR` - PTR
                * `TLSA` - TLSA
                * `SSHFP` - SSHFP
                * `HTTPS` - HTTPS
                * `SVCB` - SVCB
                * `ALIAS` - ALIAS
                * `NAPTR` - NAPTR
            ttl (int | Unset):
            priority (int | None | Unset): Priority for MX and SRV records.
    """

    id: str
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[DNSRecordListActiveConditionInstancesItem]
    organization: DNSRecordListOrganizationType0 | None
    organization_priority: bool
    workspace: DNSRecordListWorkspaceType0 | None
    created: DNSRecordListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    dns_zone: DNSZoneSimple
    content: str
    type_: DNSRecordTypeEnum | Unset = UNSET
    ttl: int | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dns_record_list_organization_type_0 import DNSRecordListOrganizationType0  # noqa: PLC0415
        from ..models.dns_record_list_workspace_type_0 import DNSRecordListWorkspaceType0  # noqa: PLC0415

        id = self.id

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
        if isinstance(self.organization, DNSRecordListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, DNSRecordListWorkspaceType0):
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

        dns_zone = self.dns_zone.to_dict()

        content = self.content

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        ttl = self.ttl

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

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
                "dns_zone": dns_zone,
                "content": content,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_record_list_active_condition_instances_item import (
            DNSRecordListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.dns_record_list_created import DNSRecordListCreated  # noqa: PLC0415
        from ..models.dns_record_list_organization_type_0 import DNSRecordListOrganizationType0  # noqa: PLC0415
        from ..models.dns_record_list_workspace_type_0 import DNSRecordListWorkspaceType0  # noqa: PLC0415
        from ..models.dns_zone_simple import DNSZoneSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = DNSRecordListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> DNSRecordListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = DNSRecordListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSRecordListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> DNSRecordListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = DNSRecordListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSRecordListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = DNSRecordListCreated.from_dict(d.pop("created"))

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

        dns_zone = DNSZoneSimple.from_dict(d.pop("dns_zone"))

        content = d.pop("content")

        _type_ = d.pop("type", UNSET)
        type_: DNSRecordTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_dns_record_type_enum(_type_)

        ttl = d.pop("ttl", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        dns_record_list = cls(
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
            dns_zone=dns_zone,
            content=content,
            type_=type_,
            ttl=ttl,
            priority=priority,
        )

        dns_record_list.additional_properties = d
        return dns_record_list

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
