from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_kind_enum import ApiKindEnum, check_api_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_account_list_active_condition_instances_item import (
        ProviderAccountListActiveConditionInstancesItem,
    )
    from ..models.provider_account_list_created import ProviderAccountListCreated
    from ..models.provider_account_list_organization_type_0 import ProviderAccountListOrganizationType0
    from ..models.provider_account_list_workspace_type_0 import ProviderAccountListWorkspaceType0


T = TypeVar("T", bound="ProviderAccountList")


@_attrs_define
class ProviderAccountList:
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
            active_condition_instances (list[ProviderAccountListActiveConditionInstancesItem]):
            organization (None | ProviderAccountListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | ProviderAccountListWorkspaceType0):
            created (ProviderAccountListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            api_kind (ApiKindEnum): * `hetzner_cloud` - Hetzner Cloud
                * `openstack` - OpenStack
                * `ovhcloud` - OVHcloud
                * `ionos` - IONOS Cloud
                * `proxmox` - Proxmox VE
                * `openai_compat` - OpenAI Compatible
                * `cloudflare` - Cloudflare DNS
            provider_entity (None | Unset | UUID): Catalog entity that owns the IaaS (e.g. Hetzner, OTC). Not
                OpenStack/Proxmox.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ProviderAccountListActiveConditionInstancesItem]
    organization: None | ProviderAccountListOrganizationType0
    organization_priority: bool
    workspace: None | ProviderAccountListWorkspaceType0
    created: ProviderAccountListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    api_kind: ApiKindEnum
    provider_entity: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_account_list_organization_type_0 import (
            ProviderAccountListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.provider_account_list_workspace_type_0 import ProviderAccountListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, ProviderAccountListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ProviderAccountListWorkspaceType0):
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

        api_kind: str = self.api_kind

        provider_entity: None | str | Unset
        if isinstance(self.provider_entity, Unset):
            provider_entity = UNSET
        elif isinstance(self.provider_entity, UUID):
            provider_entity = str(self.provider_entity)
        else:
            provider_entity = self.provider_entity

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
                "api_kind": api_kind,
            }
        )
        if provider_entity is not UNSET:
            field_dict["provider_entity"] = provider_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_account_list_active_condition_instances_item import (
            ProviderAccountListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.provider_account_list_created import ProviderAccountListCreated  # noqa: PLC0415
        from ..models.provider_account_list_organization_type_0 import (
            ProviderAccountListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.provider_account_list_workspace_type_0 import ProviderAccountListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = ProviderAccountListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | ProviderAccountListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ProviderAccountListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderAccountListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | ProviderAccountListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ProviderAccountListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderAccountListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ProviderAccountListCreated.from_dict(d.pop("created"))

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

        api_kind = check_api_kind_enum(d.pop("api_kind"))

        def _parse_provider_entity(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_entity_type_0 = UUID(data)

                return provider_entity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        provider_entity = _parse_provider_entity(d.pop("provider_entity", UNSET))

        provider_account_list = cls(
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
            api_kind=api_kind,
            provider_entity=provider_entity,
        )

        provider_account_list.additional_properties = d
        return provider_account_list

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
