from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bootstrap_status_enum import BootstrapStatusEnum, check_bootstrap_status_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.role_28f_enum import Role28FEnum, check_role_28f_enum

if TYPE_CHECKING:
    from ..models.host_list_active_condition_instances_item import HostListActiveConditionInstancesItem
    from ..models.host_list_created import HostListCreated
    from ..models.host_list_organization_type_0 import HostListOrganizationType0
    from ..models.host_list_workspace_type_0 import HostListWorkspaceType0


T = TypeVar("T", bound="HostList")


@_attrs_define
class HostList:
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
            active_condition_instances (list[HostListActiveConditionInstancesItem]):
            organization (HostListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (HostListWorkspaceType0 | None):
            created (HostListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            role (Role28FEnum): * `k8s-worker` - Kubernetes Worker
                * `k8s-controlplane` - Kubernetes Controlplane
                * `generic` - Generic
            bootstrap_status (BootstrapStatusEnum): * `pending` - Pending
                * `provisioning` - Provisioning
                * `ready` - Ready
                * `joining` - Joining
                * `failed` - Failed
                * `deprovisioning` - Deprovisioning
            provider_account (None | UUID): When set, Host is IaaS-managed via this account. Spec: polycrate spec inspect
                729.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[HostListActiveConditionInstancesItem]
    organization: HostListOrganizationType0 | None
    organization_priority: bool
    workspace: HostListWorkspaceType0 | None
    created: HostListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    role: Role28FEnum
    bootstrap_status: BootstrapStatusEnum
    provider_account: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.host_list_organization_type_0 import HostListOrganizationType0  # noqa: PLC0415
        from ..models.host_list_workspace_type_0 import HostListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, HostListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, HostListWorkspaceType0):
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

        role: str = self.role

        bootstrap_status: str = self.bootstrap_status

        provider_account: None | str
        if isinstance(self.provider_account, UUID):
            provider_account = str(self.provider_account)
        else:
            provider_account = self.provider_account

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
                "role": role,
                "bootstrap_status": bootstrap_status,
                "provider_account": provider_account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_list_active_condition_instances_item import (
            HostListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.host_list_created import HostListCreated  # noqa: PLC0415
        from ..models.host_list_organization_type_0 import HostListOrganizationType0  # noqa: PLC0415
        from ..models.host_list_workspace_type_0 import HostListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = HostListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> HostListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = HostListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> HostListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = HostListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HostListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = HostListCreated.from_dict(d.pop("created"))

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

        role = check_role_28f_enum(d.pop("role"))

        bootstrap_status = check_bootstrap_status_enum(d.pop("bootstrap_status"))

        def _parse_provider_account(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_account_type_0 = UUID(data)

                return provider_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        provider_account = _parse_provider_account(d.pop("provider_account"))

        host_list = cls(
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
            role=role,
            bootstrap_status=bootstrap_status,
            provider_account=provider_account,
        )

        host_list.additional_properties = d
        return host_list

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
