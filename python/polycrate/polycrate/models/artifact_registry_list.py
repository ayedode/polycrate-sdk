from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.artifact_registry_list_active_condition_instances_item import (
        ArtifactRegistryListActiveConditionInstancesItem,
    )
    from ..models.artifact_registry_list_created import ArtifactRegistryListCreated
    from ..models.artifact_registry_list_k8s_cluster import ArtifactRegistryListK8SCluster
    from ..models.artifact_registry_list_organization_type_0 import ArtifactRegistryListOrganizationType0
    from ..models.artifact_registry_list_workspace_type_0 import ArtifactRegistryListWorkspaceType0


T = TypeVar("T", bound="ArtifactRegistryList")


@_attrs_define
class ArtifactRegistryList:
    """List serializer for ArtifactRegistry - V2 Dynamic Tables.

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
        active_condition_instances (list[ArtifactRegistryListActiveConditionInstancesItem]):
        organization (ArtifactRegistryListOrganizationType0 | None):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (ArtifactRegistryListWorkspaceType0 | None):
        created (ArtifactRegistryListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        kind (str):
        hostname (str):
        projects_count (int):
        repositories_count (int):
        k8s_cluster (ArtifactRegistryListK8SCluster):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ArtifactRegistryListActiveConditionInstancesItem]
    organization: ArtifactRegistryListOrganizationType0 | None
    organization_priority: bool
    workspace: ArtifactRegistryListWorkspaceType0 | None
    created: ArtifactRegistryListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: str
    hostname: str
    projects_count: int
    repositories_count: int
    k8s_cluster: ArtifactRegistryListK8SCluster
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.artifact_registry_list_organization_type_0 import (
            ArtifactRegistryListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.artifact_registry_list_workspace_type_0 import ArtifactRegistryListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, ArtifactRegistryListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ArtifactRegistryListWorkspaceType0):
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

        kind = self.kind

        hostname = self.hostname

        projects_count = self.projects_count

        repositories_count = self.repositories_count

        k8s_cluster = self.k8s_cluster.to_dict()

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
                "kind": kind,
                "hostname": hostname,
                "projects_count": projects_count,
                "repositories_count": repositories_count,
                "k8s_cluster": k8s_cluster,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact_registry_list_active_condition_instances_item import (
            ArtifactRegistryListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.artifact_registry_list_created import ArtifactRegistryListCreated  # noqa: PLC0415
        from ..models.artifact_registry_list_k8s_cluster import ArtifactRegistryListK8SCluster  # noqa: PLC0415
        from ..models.artifact_registry_list_organization_type_0 import (
            ArtifactRegistryListOrganizationType0,  # noqa: PLC0415
        )
        from ..models.artifact_registry_list_workspace_type_0 import ArtifactRegistryListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = ArtifactRegistryListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> ArtifactRegistryListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ArtifactRegistryListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArtifactRegistryListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> ArtifactRegistryListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ArtifactRegistryListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArtifactRegistryListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ArtifactRegistryListCreated.from_dict(d.pop("created"))

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

        kind = d.pop("kind")

        hostname = d.pop("hostname")

        projects_count = d.pop("projects_count")

        repositories_count = d.pop("repositories_count")

        k8s_cluster = ArtifactRegistryListK8SCluster.from_dict(d.pop("k8s_cluster"))

        artifact_registry_list = cls(
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
            kind=kind,
            hostname=hostname,
            projects_count=projects_count,
            repositories_count=repositories_count,
            k8s_cluster=k8s_cluster,
        )

        artifact_registry_list.additional_properties = d
        return artifact_registry_list

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
