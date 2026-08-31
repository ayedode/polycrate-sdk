from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.downtime_kind_enum import DowntimeKindEnum, check_downtime_kind_enum
from ..models.downtime_severity_enum import DowntimeSeverityEnum, check_downtime_severity_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDowntimeRequest")


@_attrs_define
class PatchedDowntimeRequest:
    """Full serializer for Downtime detail view.

    Attributes:
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
        post_mortem_note_id (None | Unset | UUID): UUID of an existing post-mortem Note to link (or null to unlink).
    """

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
    post_mortem_note_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        post_mortem_note_id: None | str | Unset
        if isinstance(self.post_mortem_note_id, Unset):
            post_mortem_note_id = UNSET
        elif isinstance(self.post_mortem_note_id, UUID):
            post_mortem_note_id = str(self.post_mortem_note_id)
        else:
            post_mortem_note_id = self.post_mortem_note_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if post_mortem_note_id is not UNSET:
            field_dict["post_mortem_note_id"] = post_mortem_note_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.severity, Unset):
            files.append(("severity", (None, str(self.severity).encode(), "text/plain")))

        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))

        if not isinstance(self.counts_towards_sla, Unset):
            files.append(("counts_towards_sla", (None, str(self.counts_towards_sla).encode(), "text/plain")))

        if not isinstance(self.excluded_reason, Unset):
            if isinstance(self.excluded_reason, str):
                files.append(("excluded_reason", (None, str(self.excluded_reason).encode(), "text/plain")))
            else:
                files.append(("excluded_reason", (None, str(self.excluded_reason).encode(), "text/plain")))

        if not isinstance(self.post_mortem_content, Unset):
            if isinstance(self.post_mortem_content, str):
                files.append(("post_mortem_content", (None, str(self.post_mortem_content).encode(), "text/plain")))
            else:
                files.append(("post_mortem_content", (None, str(self.post_mortem_content).encode(), "text/plain")))

        if not isinstance(self.post_mortem_note_id, Unset):
            if isinstance(self.post_mortem_note_id, UUID):
                files.append(("post_mortem_note_id", (None, str(self.post_mortem_note_id), "text/plain")))
            else:
                files.append(("post_mortem_note_id", (None, str(self.post_mortem_note_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        def _parse_post_mortem_note_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_mortem_note_id_type_0 = UUID(data)

                return post_mortem_note_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        post_mortem_note_id = _parse_post_mortem_note_id(d.pop("post_mortem_note_id", UNSET))

        patched_downtime_request = cls(
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
            post_mortem_note_id=post_mortem_note_id,
        )

        patched_downtime_request.additional_properties = d
        return patched_downtime_request

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
