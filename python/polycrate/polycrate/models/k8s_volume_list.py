from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.phase_enum import PhaseEnum, check_phase_enum

if TYPE_CHECKING:
    from ..models.k8s_app_simple import K8SAppSimple
    from ..models.k8s_cluster_simple import K8SClusterSimple
    from ..models.k8s_volume_list_active_condition_instances_item import K8SVolumeListActiveConditionInstancesItem
    from ..models.k8s_volume_list_created import K8SVolumeListCreated
    from ..models.k8s_volume_list_organization_type_0 import K8SVolumeListOrganizationType0
    from ..models.k8s_volume_list_workspace_type_0 import K8SVolumeListWorkspaceType0


T = TypeVar("T", bound="K8SVolumeList")


@_attrs_define
class K8SVolumeList:
    """K8sVolume List Serializer — V2 Dynamic Tables.
    Spec: polycrate spec inspect 31

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
            active_condition_instances (list[K8SVolumeListActiveConditionInstancesItem]):
            organization (K8SVolumeListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (K8SVolumeListWorkspaceType0 | None):
            created (K8SVolumeListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            phase (PhaseEnum): * `Bound` - Bound
                * `Released` - Released
                * `Available` - Available
                * `Failed` - Failed
                * `Pending` - Pending
                * `Unknown` - Unknown
            storage_class (None | str):
            capacity_bytes (int | None):
            capacity_string (None | str): Original k8s Quantity string e.g. '10Gi', '500Mi'
            capacity_display (None | str):
            pvc_name (None | str):
            pvc_namespace (None | str):
            k8s_cluster (K8SClusterSimple):
            k8s_app (K8SAppSimple): Simple serializer for embedding K8sApp in other serializers.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[K8SVolumeListActiveConditionInstancesItem]
    organization: K8SVolumeListOrganizationType0 | None
    organization_priority: bool
    workspace: K8SVolumeListWorkspaceType0 | None
    created: K8SVolumeListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    phase: PhaseEnum
    storage_class: None | str
    capacity_bytes: int | None
    capacity_string: None | str
    capacity_display: None | str
    pvc_name: None | str
    pvc_namespace: None | str
    k8s_cluster: K8SClusterSimple
    k8s_app: K8SAppSimple
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_volume_list_organization_type_0 import K8SVolumeListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_volume_list_workspace_type_0 import K8SVolumeListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, K8SVolumeListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SVolumeListWorkspaceType0):
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

        phase: str = self.phase

        storage_class: None | str
        storage_class = self.storage_class

        capacity_bytes: int | None
        capacity_bytes = self.capacity_bytes

        capacity_string: None | str
        capacity_string = self.capacity_string

        capacity_display: None | str
        capacity_display = self.capacity_display

        pvc_name: None | str
        pvc_name = self.pvc_name

        pvc_namespace: None | str
        pvc_namespace = self.pvc_namespace

        k8s_cluster = self.k8s_cluster.to_dict()

        k8s_app = self.k8s_app.to_dict()

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
                "phase": phase,
                "storage_class": storage_class,
                "capacity_bytes": capacity_bytes,
                "capacity_string": capacity_string,
                "capacity_display": capacity_display,
                "pvc_name": pvc_name,
                "pvc_namespace": pvc_namespace,
                "k8s_cluster": k8s_cluster,
                "k8s_app": k8s_app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_app_simple import K8SAppSimple  # noqa: PLC0415
        from ..models.k8s_cluster_simple import K8SClusterSimple  # noqa: PLC0415
        from ..models.k8s_volume_list_active_condition_instances_item import (
            K8SVolumeListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.k8s_volume_list_created import K8SVolumeListCreated  # noqa: PLC0415
        from ..models.k8s_volume_list_organization_type_0 import K8SVolumeListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_volume_list_workspace_type_0 import K8SVolumeListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = K8SVolumeListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> K8SVolumeListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SVolumeListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SVolumeListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> K8SVolumeListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SVolumeListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SVolumeListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SVolumeListCreated.from_dict(d.pop("created"))

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

        phase = check_phase_enum(d.pop("phase"))

        def _parse_storage_class(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        storage_class = _parse_storage_class(d.pop("storage_class"))

        def _parse_capacity_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacity_bytes"))

        def _parse_capacity_string(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        capacity_string = _parse_capacity_string(d.pop("capacity_string"))

        def _parse_capacity_display(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        capacity_display = _parse_capacity_display(d.pop("capacity_display"))

        def _parse_pvc_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pvc_name = _parse_pvc_name(d.pop("pvc_name"))

        def _parse_pvc_namespace(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pvc_namespace = _parse_pvc_namespace(d.pop("pvc_namespace"))

        k8s_cluster = K8SClusterSimple.from_dict(d.pop("k8s_cluster"))

        k8s_app = K8SAppSimple.from_dict(d.pop("k8s_app"))

        k8s_volume_list = cls(
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
            phase=phase,
            storage_class=storage_class,
            capacity_bytes=capacity_bytes,
            capacity_string=capacity_string,
            capacity_display=capacity_display,
            pvc_name=pvc_name,
            pvc_namespace=pvc_namespace,
            k8s_cluster=k8s_cluster,
            k8s_app=k8s_app,
        )

        k8s_volume_list.additional_properties = d
        return k8s_volume_list

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
