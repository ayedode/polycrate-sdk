from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.note_kind_enum import NoteKindEnum, check_note_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedNoteRequest")


@_attrs_define
class PatchedNoteRequest:
    """Full serializer for Note detail views and CRUD operations.

    Includes complete related object data and computed fields.

        Attributes:
            name (str | Unset): Object name
            display_name (str | Unset): Human-readable name for the note
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (ProviderEnum | Unset): * `loopback` - Loopback
                * `hetzner_cloud` - HETZNER Cloud
                * `hetzner_robot` - HETZNER Robot
                * `bare_metal` - Bare-Metal
                * `powerdns` - PowerDNS
                * `cloudflare` - Cloudflare
                * `rook-ceph` - Rook Ceph
                * `polycrate` - Polycrate
                * `kubernetes` - Kubernetes
                * `helm` - Helm
                * `generic` - Generic
                * `victorialogs` - VictoriaLogs
                * `system` - System
            provider_reference (None | str | Unset):
            provider_id (None | str | Unset):
            reconciliation_enabled (bool | Unset):
            platform_service (bool | Unset):
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
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            content (str | Unset): The note content/text (Markdown)
            structured_content (Any | Unset): BlockNote JSON blocks for rich-text editing
            resolved (bool | Unset): Whether this note/task is resolved
            organization_id (None | Unset | UUID):
            workspace_id (None | Unset | UUID):
            credential_id (None | Unset | UUID):
            parent_note_id (None | Unset | UUID):
            time_tracked_hours (None | str | Unset):
            assigned_to_ids (list[int] | Unset):
            remind_at (datetime.datetime | None | Unset):
            tracked_at (datetime.datetime | None | Unset):
            project_id (None | Unset | UUID):
            vydeo_enabled (bool | Unset): Whether Vydeo meeting integration is enabled for this note
            additional_recipients (Any | Unset): Additional email addresses to invite to the Vydeo meeting (non-assignees)
            meeting_duration_minutes (int | Unset): Duration of the meeting in minutes (used to calculate valid_until for
                Vydeo invitations)
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: NoteKindEnum | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    content: str | Unset = UNSET
    structured_content: Any | Unset = UNSET
    resolved: bool | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    workspace_id: None | Unset | UUID = UNSET
    credential_id: None | Unset | UUID = UNSET
    parent_note_id: None | Unset | UUID = UNSET
    time_tracked_hours: None | str | Unset = UNSET
    assigned_to_ids: list[int] | Unset = UNSET
    remind_at: datetime.datetime | None | Unset = UNSET
    tracked_at: datetime.datetime | None | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    vydeo_enabled: bool | Unset = UNSET
    additional_recipients: Any | Unset = UNSET
    meeting_duration_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        debug_mode = self.debug_mode

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        provider_reference: None | str | Unset
        if isinstance(self.provider_reference, Unset):
            provider_reference = UNSET
        else:
            provider_reference = self.provider_reference

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        reconciliation_enabled = self.reconciliation_enabled

        platform_service = self.platform_service

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        tolerations = self.tolerations

        archived = self.archived

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        archived_reason: None | str | Unset
        if isinstance(self.archived_reason, Unset):
            archived_reason = UNSET
        else:
            archived_reason = self.archived_reason

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_availability = self.sla_availability

        content = self.content

        structured_content = self.structured_content

        resolved = self.resolved

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        elif isinstance(self.workspace_id, UUID):
            workspace_id = str(self.workspace_id)
        else:
            workspace_id = self.workspace_id

        credential_id: None | str | Unset
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        elif isinstance(self.credential_id, UUID):
            credential_id = str(self.credential_id)
        else:
            credential_id = self.credential_id

        parent_note_id: None | str | Unset
        if isinstance(self.parent_note_id, Unset):
            parent_note_id = UNSET
        elif isinstance(self.parent_note_id, UUID):
            parent_note_id = str(self.parent_note_id)
        else:
            parent_note_id = self.parent_note_id

        time_tracked_hours: None | str | Unset
        if isinstance(self.time_tracked_hours, Unset):
            time_tracked_hours = UNSET
        else:
            time_tracked_hours = self.time_tracked_hours

        assigned_to_ids: list[int] | Unset = UNSET
        if not isinstance(self.assigned_to_ids, Unset):
            assigned_to_ids = self.assigned_to_ids

        remind_at: None | str | Unset
        if isinstance(self.remind_at, Unset):
            remind_at = UNSET
        elif isinstance(self.remind_at, datetime.datetime):
            remind_at = self.remind_at.isoformat()
        else:
            remind_at = self.remind_at

        tracked_at: None | str | Unset
        if isinstance(self.tracked_at, Unset):
            tracked_at = UNSET
        elif isinstance(self.tracked_at, datetime.datetime):
            tracked_at = self.tracked_at.isoformat()
        else:
            tracked_at = self.tracked_at

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        vydeo_enabled = self.vydeo_enabled

        additional_recipients = self.additional_recipients

        meeting_duration_minutes = self.meeting_duration_minutes

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
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_reference is not UNSET:
            field_dict["provider_reference"] = provider_reference
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if content is not UNSET:
            field_dict["content"] = content
        if structured_content is not UNSET:
            field_dict["structured_content"] = structured_content
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if parent_note_id is not UNSET:
            field_dict["parent_note_id"] = parent_note_id
        if time_tracked_hours is not UNSET:
            field_dict["time_tracked_hours"] = time_tracked_hours
        if assigned_to_ids is not UNSET:
            field_dict["assigned_to_ids"] = assigned_to_ids
        if remind_at is not UNSET:
            field_dict["remind_at"] = remind_at
        if tracked_at is not UNSET:
            field_dict["tracked_at"] = tracked_at
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if vydeo_enabled is not UNSET:
            field_dict["vydeo_enabled"] = vydeo_enabled
        if additional_recipients is not UNSET:
            field_dict["additional_recipients"] = additional_recipients
        if meeting_duration_minutes is not UNSET:
            field_dict["meeting_duration_minutes"] = meeting_duration_minutes

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.debug_mode, Unset):
            files.append(("debug_mode", (None, str(self.debug_mode).encode(), "text/plain")))

        if not isinstance(self.provider, Unset):
            files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        if not isinstance(self.provider_reference, Unset):
            if isinstance(self.provider_reference, str):
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))
            else:
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

        if not isinstance(self.archived, Unset):
            files.append(("archived", (None, str(self.archived).encode(), "text/plain")))

        if not isinstance(self.archived_at, Unset):
            if isinstance(self.archived_at, datetime.datetime):
                files.append(("archived_at", (None, self.archived_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("archived_at", (None, str(self.archived_at).encode(), "text/plain")))

        if not isinstance(self.archived_reason, Unset):
            if isinstance(self.archived_reason, str):
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))
            else:
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.target_availability, Unset):
            if isinstance(self.target_availability, str):
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))
            else:
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))

        if not isinstance(self.slo_target, Unset):
            if isinstance(self.slo_target, str):
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))
            else:
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.structured_content, Unset):
            files.append(("structured_content", (None, str(self.structured_content).encode(), "text/plain")))

        if not isinstance(self.resolved, Unset):
            files.append(("resolved", (None, str(self.resolved).encode(), "text/plain")))

        if not isinstance(self.organization_id, Unset):
            if isinstance(self.organization_id, UUID):
                files.append(("organization_id", (None, str(self.organization_id), "text/plain")))
            else:
                files.append(("organization_id", (None, str(self.organization_id).encode(), "text/plain")))

        if not isinstance(self.workspace_id, Unset):
            if isinstance(self.workspace_id, UUID):
                files.append(("workspace_id", (None, str(self.workspace_id), "text/plain")))
            else:
                files.append(("workspace_id", (None, str(self.workspace_id).encode(), "text/plain")))

        if not isinstance(self.credential_id, Unset):
            if isinstance(self.credential_id, UUID):
                files.append(("credential_id", (None, str(self.credential_id), "text/plain")))
            else:
                files.append(("credential_id", (None, str(self.credential_id).encode(), "text/plain")))

        if not isinstance(self.parent_note_id, Unset):
            if isinstance(self.parent_note_id, UUID):
                files.append(("parent_note_id", (None, str(self.parent_note_id), "text/plain")))
            else:
                files.append(("parent_note_id", (None, str(self.parent_note_id).encode(), "text/plain")))

        if not isinstance(self.time_tracked_hours, Unset):
            if isinstance(self.time_tracked_hours, str):
                files.append(("time_tracked_hours", (None, str(self.time_tracked_hours).encode(), "text/plain")))
            else:
                files.append(("time_tracked_hours", (None, str(self.time_tracked_hours).encode(), "text/plain")))

        if not isinstance(self.assigned_to_ids, Unset):
            for assigned_to_ids_item_element in self.assigned_to_ids:
                files.append(("assigned_to_ids", (None, str(assigned_to_ids_item_element).encode(), "text/plain")))

        if not isinstance(self.remind_at, Unset):
            if isinstance(self.remind_at, datetime.datetime):
                files.append(("remind_at", (None, self.remind_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("remind_at", (None, str(self.remind_at).encode(), "text/plain")))

        if not isinstance(self.tracked_at, Unset):
            if isinstance(self.tracked_at, datetime.datetime):
                files.append(("tracked_at", (None, self.tracked_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("tracked_at", (None, str(self.tracked_at).encode(), "text/plain")))

        if not isinstance(self.project_id, Unset):
            if isinstance(self.project_id, UUID):
                files.append(("project_id", (None, str(self.project_id), "text/plain")))
            else:
                files.append(("project_id", (None, str(self.project_id).encode(), "text/plain")))

        if not isinstance(self.vydeo_enabled, Unset):
            files.append(("vydeo_enabled", (None, str(self.vydeo_enabled).encode(), "text/plain")))

        if not isinstance(self.additional_recipients, Unset):
            files.append(("additional_recipients", (None, str(self.additional_recipients).encode(), "text/plain")))

        if not isinstance(self.meeting_duration_minutes, Unset):
            files.append(
                ("meeting_duration_minutes", (None, str(self.meeting_duration_minutes).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        debug_mode = d.pop("debug_mode", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderEnum | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_enum(_provider)

        def _parse_provider_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference", UNSET))

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: NoteKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_note_kind_enum(_kind)

        tolerations = d.pop("tolerations", UNSET)

        archived = d.pop("archived", UNSET)

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_archived_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archived_reason = _parse_archived_reason(d.pop("archived_reason", UNSET))

        def _parse_criticality(data: object) -> BlankEnum | CriticalityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_0 = check_criticality_enum(data)

                return criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_blank_enum(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CriticalityEnum | None | Unset, data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        content = d.pop("content", UNSET)

        structured_content = d.pop("structured_content", UNSET)

        resolved = d.pop("resolved", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_workspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_id_type_0 = UUID(data)

                return workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id", UNSET))

        def _parse_credential_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_id_type_0 = UUID(data)

                return credential_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential_id = _parse_credential_id(d.pop("credential_id", UNSET))

        def _parse_parent_note_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_note_id_type_0 = UUID(data)

                return parent_note_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_note_id = _parse_parent_note_id(d.pop("parent_note_id", UNSET))

        def _parse_time_tracked_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_tracked_hours = _parse_time_tracked_hours(d.pop("time_tracked_hours", UNSET))

        assigned_to_ids = cast(list[int], d.pop("assigned_to_ids", UNSET))

        def _parse_remind_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                remind_at_type_0 = datetime.datetime.fromisoformat(data)

                return remind_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        remind_at = _parse_remind_at(d.pop("remind_at", UNSET))

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

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        vydeo_enabled = d.pop("vydeo_enabled", UNSET)

        additional_recipients = d.pop("additional_recipients", UNSET)

        meeting_duration_minutes = d.pop("meeting_duration_minutes", UNSET)

        patched_note_request = cls(
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            platform_service=platform_service,
            kind=kind,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            content=content,
            structured_content=structured_content,
            resolved=resolved,
            organization_id=organization_id,
            workspace_id=workspace_id,
            credential_id=credential_id,
            parent_note_id=parent_note_id,
            time_tracked_hours=time_tracked_hours,
            assigned_to_ids=assigned_to_ids,
            remind_at=remind_at,
            tracked_at=tracked_at,
            project_id=project_id,
            vydeo_enabled=vydeo_enabled,
            additional_recipients=additional_recipients,
            meeting_duration_minutes=meeting_duration_minutes,
        )

        patched_note_request.additional_properties = d
        return patched_note_request

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
