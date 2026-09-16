from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.k8s_addon_list_active_condition_instances_item import K8SAddonListActiveConditionInstancesItem
    from ..models.k8s_addon_list_available_versions_item import K8SAddonListAvailableVersionsItem
    from ..models.k8s_addon_list_catalogue_app_type_0 import K8SAddonListCatalogueAppType0
    from ..models.k8s_addon_list_created import K8SAddonListCreated
    from ..models.k8s_addon_list_organization_type_0 import K8SAddonListOrganizationType0
    from ..models.k8s_addon_list_workspace_type_0 import K8SAddonListWorkspaceType0


T = TypeVar("T", bound="K8SAddonList")


@_attrs_define
class K8SAddonList:
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
            active_condition_instances (list[K8SAddonListActiveConditionInstancesItem]):
            organization (K8SAddonListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (K8SAddonListWorkspaceType0 | None):
            created (K8SAddonListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            catalogue_app (K8SAddonListCatalogueAppType0 | None):
            block_name (str):
            default_version (str):
            resolved_default_version (str):
            available_versions (list[K8SAddonListAvailableVersionsItem]):
            default_block_config_template (str):
            is_default (bool):
            allow_multiple (bool):
            order (int):
            enforcement (str):
            icon_url (str):
            is_class_icon (bool):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[K8SAddonListActiveConditionInstancesItem]
    organization: K8SAddonListOrganizationType0 | None
    organization_priority: bool
    workspace: K8SAddonListWorkspaceType0 | None
    created: K8SAddonListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    catalogue_app: K8SAddonListCatalogueAppType0 | None
    block_name: str
    default_version: str
    resolved_default_version: str
    available_versions: list[K8SAddonListAvailableVersionsItem]
    default_block_config_template: str
    is_default: bool
    allow_multiple: bool
    order: int
    enforcement: str
    icon_url: str
    is_class_icon: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_addon_list_catalogue_app_type_0 import K8SAddonListCatalogueAppType0  # noqa: PLC0415
        from ..models.k8s_addon_list_organization_type_0 import K8SAddonListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_addon_list_workspace_type_0 import K8SAddonListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, K8SAddonListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SAddonListWorkspaceType0):
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

        catalogue_app: dict[str, Any] | None
        if isinstance(self.catalogue_app, K8SAddonListCatalogueAppType0):
            catalogue_app = self.catalogue_app.to_dict()
        else:
            catalogue_app = self.catalogue_app

        block_name = self.block_name

        default_version = self.default_version

        resolved_default_version = self.resolved_default_version

        available_versions = []
        for available_versions_item_data in self.available_versions:
            available_versions_item = available_versions_item_data.to_dict()
            available_versions.append(available_versions_item)

        default_block_config_template = self.default_block_config_template

        is_default = self.is_default

        allow_multiple = self.allow_multiple

        order = self.order

        enforcement = self.enforcement

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

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
                "catalogue_app": catalogue_app,
                "block_name": block_name,
                "default_version": default_version,
                "resolved_default_version": resolved_default_version,
                "available_versions": available_versions,
                "default_block_config_template": default_block_config_template,
                "is_default": is_default,
                "allow_multiple": allow_multiple,
                "order": order,
                "enforcement": enforcement,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_addon_list_active_condition_instances_item import (
            K8SAddonListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.k8s_addon_list_available_versions_item import K8SAddonListAvailableVersionsItem  # noqa: PLC0415
        from ..models.k8s_addon_list_catalogue_app_type_0 import K8SAddonListCatalogueAppType0  # noqa: PLC0415
        from ..models.k8s_addon_list_created import K8SAddonListCreated  # noqa: PLC0415
        from ..models.k8s_addon_list_organization_type_0 import K8SAddonListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_addon_list_workspace_type_0 import K8SAddonListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = K8SAddonListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> K8SAddonListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SAddonListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAddonListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> K8SAddonListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SAddonListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAddonListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SAddonListCreated.from_dict(d.pop("created"))

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

        def _parse_catalogue_app(data: object) -> K8SAddonListCatalogueAppType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                catalogue_app_type_0 = K8SAddonListCatalogueAppType0.from_dict(data)

                return catalogue_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAddonListCatalogueAppType0 | None, data)

        catalogue_app = _parse_catalogue_app(d.pop("catalogue_app"))

        block_name = d.pop("block_name")

        default_version = d.pop("default_version")

        resolved_default_version = d.pop("resolved_default_version")

        available_versions = []
        _available_versions = d.pop("available_versions")
        for available_versions_item_data in _available_versions:
            available_versions_item = K8SAddonListAvailableVersionsItem.from_dict(available_versions_item_data)

            available_versions.append(available_versions_item)

        default_block_config_template = d.pop("default_block_config_template")

        is_default = d.pop("is_default")

        allow_multiple = d.pop("allow_multiple")

        order = d.pop("order")

        enforcement = d.pop("enforcement")

        icon_url = d.pop("icon_url")

        is_class_icon = d.pop("is_class_icon")

        k8s_addon_list = cls(
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
            catalogue_app=catalogue_app,
            block_name=block_name,
            default_version=default_version,
            resolved_default_version=resolved_default_version,
            available_versions=available_versions,
            default_block_config_template=default_block_config_template,
            is_default=is_default,
            allow_multiple=allow_multiple,
            order=order,
            enforcement=enforcement,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
        )

        k8s_addon_list.additional_properties = d
        return k8s_addon_list

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
