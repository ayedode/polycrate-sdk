from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.note_kind_enum import NoteKindEnum, check_note_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_list_active_condition_instances_item import NoteListActiveConditionInstancesItem
    from ..models.note_list_assignees_item import NoteListAssigneesItem
    from ..models.note_list_created import NoteListCreated
    from ..models.note_list_created_by_user_type_0 import NoteListCreatedByUserType0
    from ..models.note_list_managed_by_type_0 import NoteListManagedByType0
    from ..models.note_list_parent_note_type_0 import NoteListParentNoteType0
    from ..models.note_list_project_type_0 import NoteListProjectType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="NoteList")


@_attrs_define
class NoteList:
    """Lightweight serializer for Note list views.

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
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[NoteListActiveConditionInstancesItem]):
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (WorkspaceSimple):
            created (NoteListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind_display (str):
            content (str): The note content/text (Markdown)
            replies_count (int):
            total_time_tracked_hours (None | str):
            assignees (list[NoteListAssigneesItem]):
            managed_by (None | NoteListManagedByType0):
            created_by_user (None | NoteListCreatedByUserType0):
            project (None | NoteListProjectType0):
            parent_note (None | NoteListParentNoteType0):
            kind (NoteKindEnum | Unset): * `info` - Information
                * `warning` - Warning
                * `todo` - Todo
                * `reminder` - Reminder
                * `comment` - Comment
                * `post-mortem` - Post-Mortem
                * `provider-status` - Provider Status
                * `news` - News
                * `object-note` - Object Note
                * `meeting` - Meeting
                * `restore-test` - Restore Test
                * `app-release` - App Release
            resolved (bool | Unset): Whether this note/task is resolved
            time_tracked_hours (None | str | Unset): Hours tracked on this comment. Only valid for kind='comment'.
            tracked_at (datetime.datetime | None | Unset): Explicit tracking date for timetracking comments. Overrides
                created_at in billing calculations. Only valid for kind='comment'.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    condition_instance_count: int
    active_condition_instances: list[NoteListActiveConditionInstancesItem]
    organization: OrganizationSimple
    organization_priority: bool
    workspace: WorkspaceSimple
    created: NoteListCreated
    archived: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind_display: str
    content: str
    replies_count: int
    total_time_tracked_hours: None | str
    assignees: list[NoteListAssigneesItem]
    managed_by: None | NoteListManagedByType0
    created_by_user: None | NoteListCreatedByUserType0
    project: None | NoteListProjectType0
    parent_note: None | NoteListParentNoteType0
    kind: NoteKindEnum | Unset = UNSET
    resolved: bool | Unset = UNSET
    time_tracked_hours: None | str | Unset = UNSET
    tracked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.note_list_created_by_user_type_0 import NoteListCreatedByUserType0
        from ..models.note_list_managed_by_type_0 import NoteListManagedByType0
        from ..models.note_list_parent_note_type_0 import NoteListParentNoteType0
        from ..models.note_list_project_type_0 import NoteListProjectType0

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

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

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind_display = self.kind_display

        content = self.content

        replies_count = self.replies_count

        total_time_tracked_hours: None | str
        total_time_tracked_hours = self.total_time_tracked_hours

        assignees = []
        for assignees_item_data in self.assignees:
            assignees_item = assignees_item_data.to_dict()
            assignees.append(assignees_item)

        managed_by: dict[str, Any] | None
        if isinstance(self.managed_by, NoteListManagedByType0):
            managed_by = self.managed_by.to_dict()
        else:
            managed_by = self.managed_by

        created_by_user: dict[str, Any] | None
        if isinstance(self.created_by_user, NoteListCreatedByUserType0):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        project: dict[str, Any] | None
        if isinstance(self.project, NoteListProjectType0):
            project = self.project.to_dict()
        else:
            project = self.project

        parent_note: dict[str, Any] | None
        if isinstance(self.parent_note, NoteListParentNoteType0):
            parent_note = self.parent_note.to_dict()
        else:
            parent_note = self.parent_note

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        resolved = self.resolved

        time_tracked_hours: None | str | Unset
        if isinstance(self.time_tracked_hours, Unset):
            time_tracked_hours = UNSET
        else:
            time_tracked_hours = self.time_tracked_hours

        tracked_at: None | str | Unset
        if isinstance(self.tracked_at, Unset):
            tracked_at = UNSET
        elif isinstance(self.tracked_at, datetime.datetime):
            tracked_at = self.tracked_at.isoformat()
        else:
            tracked_at = self.tracked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "effective_criticality": effective_criticality,
                "url": url,
                "kind_display": kind_display,
                "content": content,
                "replies_count": replies_count,
                "total_time_tracked_hours": total_time_tracked_hours,
                "assignees": assignees,
                "managed_by": managed_by,
                "created_by_user": created_by_user,
                "project": project,
                "parent_note": parent_note,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if time_tracked_hours is not UNSET:
            field_dict["time_tracked_hours"] = time_tracked_hours
        if tracked_at is not UNSET:
            field_dict["tracked_at"] = tracked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.note_list_active_condition_instances_item import NoteListActiveConditionInstancesItem
        from ..models.note_list_assignees_item import NoteListAssigneesItem
        from ..models.note_list_created import NoteListCreated
        from ..models.note_list_created_by_user_type_0 import NoteListCreatedByUserType0
        from ..models.note_list_managed_by_type_0 import NoteListManagedByType0
        from ..models.note_list_parent_note_type_0 import NoteListParentNoteType0
        from ..models.note_list_project_type_0 import NoteListProjectType0
        from ..models.organization_simple import OrganizationSimple
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = NoteListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = NoteListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

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

        content = d.pop("content")

        replies_count = d.pop("replies_count")

        def _parse_total_time_tracked_hours(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        total_time_tracked_hours = _parse_total_time_tracked_hours(d.pop("total_time_tracked_hours"))

        assignees = []
        _assignees = d.pop("assignees")
        for assignees_item_data in _assignees:
            assignees_item = NoteListAssigneesItem.from_dict(assignees_item_data)

            assignees.append(assignees_item)

        def _parse_managed_by(data: object) -> None | NoteListManagedByType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                managed_by_type_0 = NoteListManagedByType0.from_dict(data)

                return managed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteListManagedByType0, data)

        managed_by = _parse_managed_by(d.pop("managed_by"))

        def _parse_created_by_user(data: object) -> None | NoteListCreatedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = NoteListCreatedByUserType0.from_dict(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteListCreatedByUserType0, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user"))

        def _parse_project(data: object) -> None | NoteListProjectType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                project_type_0 = NoteListProjectType0.from_dict(data)

                return project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteListProjectType0, data)

        project = _parse_project(d.pop("project"))

        def _parse_parent_note(data: object) -> None | NoteListParentNoteType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_note_type_0 = NoteListParentNoteType0.from_dict(data)

                return parent_note_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NoteListParentNoteType0, data)

        parent_note = _parse_parent_note(d.pop("parent_note"))

        _kind = d.pop("kind", UNSET)
        kind: NoteKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_note_kind_enum(_kind)

        resolved = d.pop("resolved", UNSET)

        def _parse_time_tracked_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_tracked_hours = _parse_time_tracked_hours(d.pop("time_tracked_hours", UNSET))

        def _parse_tracked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tracked_at_type_0 = datetime.datetime.fromisoformat(data)

                return tracked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        tracked_at = _parse_tracked_at(d.pop("tracked_at", UNSET))

        note_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            effective_criticality=effective_criticality,
            url=url,
            kind_display=kind_display,
            content=content,
            replies_count=replies_count,
            total_time_tracked_hours=total_time_tracked_hours,
            assignees=assignees,
            managed_by=managed_by,
            created_by_user=created_by_user,
            project=project,
            parent_note=parent_note,
            kind=kind,
            resolved=resolved,
            time_tracked_hours=time_tracked_hours,
            tracked_at=tracked_at,
        )

        note_list.additional_properties = d
        return note_list

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
