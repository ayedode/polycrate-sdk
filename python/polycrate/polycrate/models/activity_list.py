from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_kind_enum import ActivityKindEnum, check_activity_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_list_active_condition_instances_item import ActivityListActiveConditionInstancesItem
    from ..models.activity_list_created import ActivityListCreated
    from ..models.activity_list_user_type_0 import ActivityListUserType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="ActivityList")


@_attrs_define
class ActivityList:
    """Lightweight serializer for Activity list views.

    Optimized for list performance with minimal related data.

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
            active_condition_instances (list[ActivityListActiveConditionInstancesItem]):
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (WorkspaceSimple):
            created (ActivityListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind_display (str):
            icon_category (str): Visual category (down|up|notification|neutral) for timeline icon rendering.
            user (ActivityListUserType0 | None):
            user_email (None | str):
            object_icon_url (str): Deterministic class icon of the referenced object, derived from object_type. Spec 484.
            kind (ActivityKindEnum | Unset): * `generic` - Generic
                * `creation` - Creation
                * `update` - Update
                * `deletion` - Deletion
                * `reconciliation` - Reconciliation
                * `discovery` - Discovery
                * `repair` - Repair
                * `check` - Check
                * `alert` - Alert
                * `announcement` - Announcement
                * `replicaset_created` - Replicaset Created
                * `statefulset_created` - Statefulset Created
                * `k8s_app_instance_installed` - K8s App Instance Installed
                * `k8s_app_instance_uninstalled` - K8s App Instance Uninstalled
                * `k8s_app_installed` - K8s App Installed
                * `k8s_app_uninstalled` - K8s App Uninstalled
                * `k8s_app_installation_failed` - K8s App Installation Failed
                * `k8s_app_uninstallation_failed` - K8s App Uninstallation Failed
                * `block_action_run` - Block Action Run
                * `block_action_run_start` - Block Action Run Start
                * `block_action_run_finish` - Block Action Run Finish
                * `condition_added` - Condition Added
                * `condition_removed` - Condition Removed
                * `state_changed` - State Changed
                * `long_running_task_detected` - Long Running Task Detected
                * `price_changed` - Price Changed
                * `product_subscribed` - Product Subscribed
                * `product_cancelled` - Product Cancelled
                * `downtime` - Downtime
                * `downtime_started` - Downtime Started
                * `downtime_ended` - Downtime Ended
                * `downtime_triggered` - Downtime Triggered
                * `downtime_updated` - Downtime Updated
                * `downtime_object_added` - Downtime Object Added
                * `downtime_object_recovered` - Downtime Object Recovered
                * `downtime_closed_manually` - Downtime Closed Manually
                * `maintenance_scheduled` - Maintenance Scheduled
                * `maintenance_started` - Maintenance Started
                * `maintenance_ended` - Maintenance Ended
                * `incident_created` - Incident Created
                * `incident_status_changed` - Incident Status Changed
                * `incident_downtime_linked` - Incident Downtime Linked
                * `incident_downtime_unlinked` - Incident Downtime Unlinked
                * `notification_sent` - Notification Sent
                * `notification_send_failed` - Notification Send Failed
                * `note_created` - Note Created
                * `note_reply` - Note Reply
                * `note_resolved` - Note Resolved
                * `note_reminder` - Note Reminder
                * `ssh-session` - SSH Session
                * `workspace-sync` - Workspace Sync
            message (None | str | Unset): Human-readable activity description
            object_type (None | str | Unset): Type of the object this activity relates to
            object_name (None | str | Unset): Name of the object this activity relates to
            object_url (None | str | Unset): URL of the object this activity relates to
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ActivityListActiveConditionInstancesItem]
    organization: OrganizationSimple
    organization_priority: bool
    workspace: WorkspaceSimple
    created: ActivityListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind_display: str
    icon_category: str
    user: ActivityListUserType0 | None
    user_email: None | str
    object_icon_url: str
    kind: ActivityKindEnum | Unset = UNSET
    message: None | str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    object_name: None | str | Unset = UNSET
    object_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_list_user_type_0 import ActivityListUserType0  # noqa: PLC0415

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

        organization = self.organization.to_dict()

        organization_priority = self.organization_priority

        workspace = self.workspace.to_dict()

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind_display = self.kind_display

        icon_category = self.icon_category

        user: dict[str, Any] | None
        if isinstance(self.user, ActivityListUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        user_email: None | str
        user_email = self.user_email

        object_icon_url = self.object_icon_url

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        object_name: None | str | Unset
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        object_url: None | str | Unset
        if isinstance(self.object_url, Unset):
            object_url = UNSET
        else:
            object_url = self.object_url

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
                "kind_display": kind_display,
                "icon_category": icon_category,
                "user": user,
                "user_email": user_email,
                "object_icon_url": object_icon_url,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if message is not UNSET:
            field_dict["message"] = message
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_name is not UNSET:
            field_dict["object_name"] = object_name
        if object_url is not UNSET:
            field_dict["object_url"] = object_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_list_active_condition_instances_item import (
            ActivityListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.activity_list_created import ActivityListCreated  # noqa: PLC0415
        from ..models.activity_list_user_type_0 import ActivityListUserType0  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

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
            active_condition_instances_item = ActivityListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = ActivityListCreated.from_dict(d.pop("created"))

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

        kind_display = d.pop("kind_display")

        icon_category = d.pop("icon_category")

        def _parse_user(data: object) -> ActivityListUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = ActivityListUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityListUserType0 | None, data)

        user = _parse_user(d.pop("user"))

        def _parse_user_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_email = _parse_user_email(d.pop("user_email"))

        object_icon_url = d.pop("object_icon_url")

        _kind = d.pop("kind", UNSET)
        kind: ActivityKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_activity_kind_enum(_kind)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_object_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_name = _parse_object_name(d.pop("object_name", UNSET))

        def _parse_object_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_url = _parse_object_url(d.pop("object_url", UNSET))

        activity_list = cls(
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
            kind_display=kind_display,
            icon_category=icon_category,
            user=user,
            user_email=user_email,
            object_icon_url=object_icon_url,
            kind=kind,
            message=message,
            object_type=object_type,
            object_name=object_name,
            object_url=object_url,
        )

        activity_list.additional_properties = d
        return activity_list

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
