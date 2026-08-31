from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.downtime_kind_enum import DowntimeKindEnum, check_downtime_kind_enum
from ..models.downtime_severity_enum import DowntimeSeverityEnum, check_downtime_severity_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.downtime_affected_object import DowntimeAffectedObject
    from ..models.downtime_affected_workspaces_item import DowntimeAffectedWorkspacesItem
    from ..models.organization_simple import OrganizationSimple
    from ..models.post_mortem_note import PostMortemNote


T = TypeVar("T", bound="Downtime")


@_attrs_define
class Downtime:
    """Full serializer for Downtime detail view.

    Attributes:
        id (UUID):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        started_at (datetime.datetime): Start of the downtime
        ended_at (datetime.datetime | None): End of the downtime (null = active)
        duration_str (str): Human-readable duration.
        post_mortem_note (PostMortemNote): Simple serializer for post-mortem note data.
        affected_objects (list[DowntimeAffectedObject]):
        affected_objects_count (int):
        affected_workspaces (list[DowntimeAffectedWorkspacesItem]):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        url (str): Gibt die absolute URL zum Object zurück.
        icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
            Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
        name (str | Unset): Object name
        display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
            from the name.
        labels (Any | Unset):
        annotations (Any | Unset):
        tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
            the condition will not be applied.
        kind (DowntimeKindEnum | Unset): * `generic` - Generic
            * `planned-maintenance` - Planned Maintenance
            * `emergency-maintenance` - Emergency Maintenance
            * `customer-caused` - Customer Caused
            * `upstream-provider` - Upstream Provider Issue
            * `force-majeure` - Force Majeure
            * `false-positive` - False Positive
        severity (DowntimeSeverityEnum | Unset): * `minor` - Minor
            * `major` - Major
            * `critical` - Critical
        is_active (bool | Unset): Whether the downtime is active and should be reconciled
        counts_towards_sla (bool | Unset): Whether this downtime counts towards SLA calculation. Automatically set based
            on 'kind'. Can be manually overridden for special cases.
        excluded_reason (None | str | Unset): Reason why this downtime does not count towards SLA (automatically
            populated based on kind)
        post_mortem_content (None | str | Unset): DEPRECATED: Use Notes with kind='post-mortem' instead. This field is
            kept for backward compatibility.
    """

    id: UUID
    organization: OrganizationSimple
    started_at: datetime.datetime
    ended_at: datetime.datetime | None
    duration_str: str
    post_mortem_note: PostMortemNote
    affected_objects: list[DowntimeAffectedObject]
    affected_objects_count: int
    affected_workspaces: list[DowntimeAffectedWorkspacesItem]
    conditions: Any
    state: LastStateEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    url: str
    icon_url: str
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    tolerations: Any | Unset = UNSET
    kind: DowntimeKindEnum | Unset = UNSET
    severity: DowntimeSeverityEnum | Unset = UNSET
    is_active: bool | Unset = UNSET
    counts_towards_sla: bool | Unset = UNSET
    excluded_reason: None | str | Unset = UNSET
    post_mortem_content: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        organization = self.organization.to_dict()

        started_at = self.started_at.isoformat()

        ended_at: None | str
        if isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        duration_str = self.duration_str

        post_mortem_note = self.post_mortem_note.to_dict()

        affected_objects = []
        for affected_objects_item_data in self.affected_objects:
            affected_objects_item = affected_objects_item_data.to_dict()
            affected_objects.append(affected_objects_item)

        affected_objects_count = self.affected_objects_count

        affected_workspaces = []
        for affected_workspaces_item_data in self.affected_workspaces:
            affected_workspaces_item = affected_workspaces_item_data.to_dict()
            affected_workspaces.append(affected_workspaces_item)

        conditions = self.conditions

        state: str = self.state

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        url = self.url

        icon_url = self.icon_url

        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        tolerations = self.tolerations

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

        is_active = self.is_active

        counts_towards_sla = self.counts_towards_sla

        excluded_reason: None | str | Unset
        if isinstance(self.excluded_reason, Unset):
            excluded_reason = UNSET
        else:
            excluded_reason = self.excluded_reason

        post_mortem_content: None | str | Unset
        if isinstance(self.post_mortem_content, Unset):
            post_mortem_content = UNSET
        else:
            post_mortem_content = self.post_mortem_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "organization": organization,
                "started_at": started_at,
                "ended_at": ended_at,
                "duration_str": duration_str,
                "post_mortem_note": post_mortem_note,
                "affected_objects": affected_objects,
                "affected_objects_count": affected_objects_count,
                "affected_workspaces": affected_workspaces,
                "conditions": conditions,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "url": url,
                "icon_url": icon_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if kind is not UNSET:
            field_dict["kind"] = kind
        if severity is not UNSET:
            field_dict["severity"] = severity
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if counts_towards_sla is not UNSET:
            field_dict["counts_towards_sla"] = counts_towards_sla
        if excluded_reason is not UNSET:
            field_dict["excluded_reason"] = excluded_reason
        if post_mortem_content is not UNSET:
            field_dict["post_mortem_content"] = post_mortem_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.downtime_affected_object import DowntimeAffectedObject
        from ..models.downtime_affected_workspaces_item import DowntimeAffectedWorkspacesItem
        from ..models.organization_simple import OrganizationSimple
        from ..models.post_mortem_note import PostMortemNote

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        def _parse_ended_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ended_at = _parse_ended_at(d.pop("ended_at"))

        duration_str = d.pop("duration_str")

        post_mortem_note = PostMortemNote.from_dict(d.pop("post_mortem_note"))

        affected_objects = []
        _affected_objects = d.pop("affected_objects")
        for affected_objects_item_data in _affected_objects:
            affected_objects_item = DowntimeAffectedObject.from_dict(affected_objects_item_data)

            affected_objects.append(affected_objects_item)

        affected_objects_count = d.pop("affected_objects_count")

        affected_workspaces = []
        _affected_workspaces = d.pop("affected_workspaces")
        for affected_workspaces_item_data in _affected_workspaces:
            affected_workspaces_item = DowntimeAffectedWorkspacesItem.from_dict(affected_workspaces_item_data)

            affected_workspaces.append(affected_workspaces_item)

        conditions = d.pop("conditions")

        state = check_last_state_enum(d.pop("state"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        icon_url = d.pop("icon_url")

        name = d.pop("name", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        tolerations = d.pop("tolerations", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: DowntimeKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_downtime_kind_enum(_kind)

        _severity = d.pop("severity", UNSET)
        severity: DowntimeSeverityEnum | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_downtime_severity_enum(_severity)

        is_active = d.pop("is_active", UNSET)

        counts_towards_sla = d.pop("counts_towards_sla", UNSET)

        def _parse_excluded_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excluded_reason = _parse_excluded_reason(d.pop("excluded_reason", UNSET))

        def _parse_post_mortem_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_mortem_content = _parse_post_mortem_content(d.pop("post_mortem_content", UNSET))

        downtime = cls(
            id=id,
            organization=organization,
            started_at=started_at,
            ended_at=ended_at,
            duration_str=duration_str,
            post_mortem_note=post_mortem_note,
            affected_objects=affected_objects,
            affected_objects_count=affected_objects_count,
            affected_workspaces=affected_workspaces,
            conditions=conditions,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            icon_url=icon_url,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            tolerations=tolerations,
            kind=kind,
            severity=severity,
            is_active=is_active,
            counts_towards_sla=counts_towards_sla,
            excluded_reason=excluded_reason,
            post_mortem_content=post_mortem_content,
        )

        downtime.additional_properties = d
        return downtime

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
