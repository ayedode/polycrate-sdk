from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.purpose_f3b_enum import PurposeF3BEnum, check_purpose_f3b_enum
from ..models.workspace_kind_enum import WorkspaceKindEnum, check_workspace_kind_enum

if TYPE_CHECKING:
    from ..models.pop_simple import PopSimple
    from ..models.workspace_list_active_condition_instances_item import WorkspaceListActiveConditionInstancesItem
    from ..models.workspace_list_created import WorkspaceListCreated
    from ..models.workspace_list_organization_type_0 import WorkspaceListOrganizationType0
    from ..models.workspace_list_workspace_type_0 import WorkspaceListWorkspaceType0


T = TypeVar("T", bound="WorkspaceList")


@_attrs_define
class WorkspaceList:
    """Workspace List Serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace (None für Workspaces), created, reconciliation_running, url

    Workspace-spezifische Felder:
    - kind, legacy, git_commit_short_sha, etc.
    - pop: Point of Presence (Spec: .specs/0.12.0/workspace-pop-required.md)
    - operator_version: Version des verbundenen Operators (Spec: .specs/0.11.27/workspace-operator-version-column.md)

    Per .specs/0.11.4/dynamic-table-v2.md

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
            active_condition_instances (list[WorkspaceListActiveConditionInstancesItem]):
            organization (None | WorkspaceListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | WorkspaceListWorkspaceType0):
            created (WorkspaceListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (WorkspaceKindEnum): * `polycrate` - Polycrate
                * `generic` - Generic
            legacy (bool): Legacy workspaces have Git-Repos, non-legacy workspaces work only with Block-Infos from Polycrate
                API/UI
            git_commit_short_sha (None | str):
            notifications_enabled (bool):
            backup_enabled (bool): If false, ayedo does not evaluate workspace-level backup health
                (WORKSPACE_BACKUP_SCHEDULE_MISSING, WORKSPACE_BACKUP_SCHEDULE_OVERDUE, WORKSPACE_BACKUP_MISSING). Use when ayedo
                is not responsible for backups. May later gate related backup features; bucket provisioning stays independent
                for now.
            metrics_enabled (bool): If false, ayedo does not auto-subscribe the VictoriaMetrics agent addon. Use when this
                workspace must not scrape or send cluster metrics.
            logs_enabled (bool): If false, ayedo does not auto-subscribe VictoriaLogs or Kubernetes Event Exporter. Use when
                this workspace must not scrape or send cluster logs.
            k8s_addons_enabled (bool): If false, cluster reconcile does not run K8s addon subscription desired-state (no
                auto-subscribe, no addon install enqueue, no addon conditions). Subscribe, promote, and the cluster Addons tab
                are unavailable. Use while this workspace is still git-managed via workspace.poly.
            git_web_url (None | str):
            git_ssh_url (None | str):
            pop (PopSimple): Simple serializer for embedding Pop in other serializers.
            operator_version (None | str):
            workspace_version (None | str):
            workspace_app_version (None | str):
            description (None | str): Short free-text description of this workspace
            purpose (None | PurposeF3BEnum): Purpose of this workspace (production, development, staging, qa,
                infrastructure, platform)

                * `production` - Production
                * `development` - Development
                * `staging` - Staging
                * `qa` - QA
                * `infrastructure` - Infrastructure
                * `platform` - Platform
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[WorkspaceListActiveConditionInstancesItem]
    organization: None | WorkspaceListOrganizationType0
    organization_priority: bool
    workspace: None | WorkspaceListWorkspaceType0
    created: WorkspaceListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: WorkspaceKindEnum
    legacy: bool
    git_commit_short_sha: None | str
    notifications_enabled: bool
    backup_enabled: bool
    metrics_enabled: bool
    logs_enabled: bool
    k8s_addons_enabled: bool
    git_web_url: None | str
    git_ssh_url: None | str
    pop: PopSimple
    operator_version: None | str
    workspace_version: None | str
    workspace_app_version: None | str
    description: None | str
    purpose: None | PurposeF3BEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workspace_list_organization_type_0 import WorkspaceListOrganizationType0  # noqa: PLC0415
        from ..models.workspace_list_workspace_type_0 import WorkspaceListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, WorkspaceListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, WorkspaceListWorkspaceType0):
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

        kind: str = self.kind

        legacy = self.legacy

        git_commit_short_sha: None | str
        git_commit_short_sha = self.git_commit_short_sha

        notifications_enabled = self.notifications_enabled

        backup_enabled = self.backup_enabled

        metrics_enabled = self.metrics_enabled

        logs_enabled = self.logs_enabled

        k8s_addons_enabled = self.k8s_addons_enabled

        git_web_url: None | str
        git_web_url = self.git_web_url

        git_ssh_url: None | str
        git_ssh_url = self.git_ssh_url

        pop = self.pop.to_dict()

        operator_version: None | str
        operator_version = self.operator_version

        workspace_version: None | str
        workspace_version = self.workspace_version

        workspace_app_version: None | str
        workspace_app_version = self.workspace_app_version

        description: None | str
        description = self.description

        purpose: None | str
        if isinstance(self.purpose, str):
            purpose = self.purpose
        else:
            purpose = self.purpose

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
                "legacy": legacy,
                "git_commit_short_sha": git_commit_short_sha,
                "notifications_enabled": notifications_enabled,
                "backup_enabled": backup_enabled,
                "metrics_enabled": metrics_enabled,
                "logs_enabled": logs_enabled,
                "k8s_addons_enabled": k8s_addons_enabled,
                "git_web_url": git_web_url,
                "git_ssh_url": git_ssh_url,
                "pop": pop,
                "operator_version": operator_version,
                "workspace_version": workspace_version,
                "workspace_app_version": workspace_app_version,
                "description": description,
                "purpose": purpose,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pop_simple import PopSimple  # noqa: PLC0415
        from ..models.workspace_list_active_condition_instances_item import (
            WorkspaceListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.workspace_list_created import WorkspaceListCreated  # noqa: PLC0415
        from ..models.workspace_list_organization_type_0 import WorkspaceListOrganizationType0  # noqa: PLC0415
        from ..models.workspace_list_workspace_type_0 import WorkspaceListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = WorkspaceListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | WorkspaceListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = WorkspaceListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | WorkspaceListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = WorkspaceListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkspaceListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = WorkspaceListCreated.from_dict(d.pop("created"))

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

        kind = check_workspace_kind_enum(d.pop("kind"))

        legacy = d.pop("legacy")

        def _parse_git_commit_short_sha(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_commit_short_sha = _parse_git_commit_short_sha(d.pop("git_commit_short_sha"))

        notifications_enabled = d.pop("notifications_enabled")

        backup_enabled = d.pop("backup_enabled")

        metrics_enabled = d.pop("metrics_enabled")

        logs_enabled = d.pop("logs_enabled")

        k8s_addons_enabled = d.pop("k8s_addons_enabled")

        def _parse_git_web_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_web_url = _parse_git_web_url(d.pop("git_web_url"))

        def _parse_git_ssh_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        git_ssh_url = _parse_git_ssh_url(d.pop("git_ssh_url"))

        pop = PopSimple.from_dict(d.pop("pop"))

        def _parse_operator_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        operator_version = _parse_operator_version(d.pop("operator_version"))

        def _parse_workspace_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_version = _parse_workspace_version(d.pop("workspace_version"))

        def _parse_workspace_app_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace_app_version = _parse_workspace_app_version(d.pop("workspace_app_version"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_purpose(data: object) -> None | PurposeF3BEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purpose_type_0 = check_purpose_f3b_enum(data)

                return purpose_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PurposeF3BEnum, data)

        purpose = _parse_purpose(d.pop("purpose"))

        workspace_list = cls(
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
            legacy=legacy,
            git_commit_short_sha=git_commit_short_sha,
            notifications_enabled=notifications_enabled,
            backup_enabled=backup_enabled,
            metrics_enabled=metrics_enabled,
            logs_enabled=logs_enabled,
            k8s_addons_enabled=k8s_addons_enabled,
            git_web_url=git_web_url,
            git_ssh_url=git_ssh_url,
            pop=pop,
            operator_version=operator_version,
            workspace_version=workspace_version,
            workspace_app_version=workspace_app_version,
            description=description,
            purpose=purpose,
        )

        workspace_list.additional_properties = d
        return workspace_list

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
