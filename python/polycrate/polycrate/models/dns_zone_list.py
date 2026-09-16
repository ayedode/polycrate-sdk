from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_zone_kind_enum import DNSZoneKindEnum, check_dns_zone_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_zone_list_active_condition_instances_item import DNSZoneListActiveConditionInstancesItem
    from ..models.dns_zone_list_created import DNSZoneListCreated
    from ..models.dns_zone_list_organization_type_0 import DNSZoneListOrganizationType0
    from ..models.dns_zone_list_workspace_type_0 import DNSZoneListWorkspaceType0


T = TypeVar("T", bound="DNSZoneList")


@_attrs_define
class DNSZoneList:
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
            active_condition_instances (list[DNSZoneListActiveConditionInstancesItem]):
            organization (DNSZoneListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (DNSZoneListWorkspaceType0 | None):
            created (DNSZoneListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            sync_from_name (str):
            mirrored (str):
            kind (DNSZoneKindEnum | Unset): * `internal` - Internal
                * `external` - External
            provider (None | str | Unset): Lexicon provider name (e.g. 'cloudflare', 'hetzner', 'route53'). Required for
                kind='external'. Immutable after creation.
            primary_zone (bool | Unset): When multiple external DNS zones share the same name in an organization (different
                providers), the primary zone is preferred for DNS01/ACME and other single-writer automations. Default true.
            sync_from (None | Unset | UUID): Mirror DNS records from this zone. When set, all records are kept in sync with
                the source zone via the reconciliation loop (5-minute interval). Target must be kind='internal'; source may be
                internal or external. Must be in the same organization.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[DNSZoneListActiveConditionInstancesItem]
    organization: DNSZoneListOrganizationType0 | None
    organization_priority: bool
    workspace: DNSZoneListWorkspaceType0 | None
    created: DNSZoneListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    sync_from_name: str
    mirrored: str
    kind: DNSZoneKindEnum | Unset = UNSET
    provider: None | str | Unset = UNSET
    primary_zone: bool | Unset = UNSET
    sync_from: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dns_zone_list_organization_type_0 import DNSZoneListOrganizationType0  # noqa: PLC0415
        from ..models.dns_zone_list_workspace_type_0 import DNSZoneListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, DNSZoneListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, DNSZoneListWorkspaceType0):
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

        sync_from_name = self.sync_from_name

        mirrored = self.mirrored

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        primary_zone = self.primary_zone

        sync_from: None | str | Unset
        if isinstance(self.sync_from, Unset):
            sync_from = UNSET
        elif isinstance(self.sync_from, UUID):
            sync_from = str(self.sync_from)
        else:
            sync_from = self.sync_from

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
                "sync_from_name": sync_from_name,
                "mirrored": mirrored,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if provider is not UNSET:
            field_dict["provider"] = provider
        if primary_zone is not UNSET:
            field_dict["primary_zone"] = primary_zone
        if sync_from is not UNSET:
            field_dict["sync_from"] = sync_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_zone_list_active_condition_instances_item import (
            DNSZoneListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.dns_zone_list_created import DNSZoneListCreated  # noqa: PLC0415
        from ..models.dns_zone_list_organization_type_0 import DNSZoneListOrganizationType0  # noqa: PLC0415
        from ..models.dns_zone_list_workspace_type_0 import DNSZoneListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = DNSZoneListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> DNSZoneListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = DNSZoneListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> DNSZoneListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = DNSZoneListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = DNSZoneListCreated.from_dict(d.pop("created"))

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

        sync_from_name = d.pop("sync_from_name")

        mirrored = d.pop("mirrored")

        _kind = d.pop("kind", UNSET)
        kind: DNSZoneKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_dns_zone_kind_enum(_kind)

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        primary_zone = d.pop("primary_zone", UNSET)

        def _parse_sync_from(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sync_from_type_0 = UUID(data)

                return sync_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sync_from = _parse_sync_from(d.pop("sync_from", UNSET))

        dns_zone_list = cls(
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
            sync_from_name=sync_from_name,
            mirrored=mirrored,
            kind=kind,
            provider=provider,
            primary_zone=primary_zone,
            sync_from=sync_from,
        )

        dns_zone_list.additional_properties = d
        return dns_zone_list

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
