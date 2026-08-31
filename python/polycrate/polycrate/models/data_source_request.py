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
from ..models.data_source_kind_enum import DataSourceKindEnum, check_data_source_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSourceRequest")


@_attrs_define
class DataSourceRequest:
    """Full detail serializer for DataSource.

    Attributes:
        name (str | Unset): Object name
        display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
            from the name.
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
        kind (DataSourceKindEnum | Unset): * `rss` - RSS/Atom Feed
            * `api` - REST API
            * `polycrate-hub` - Polycrate Hub
            * `otc-status` - Open Telekom Cloud Status
            * `webhook` - Webhook
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
        datasource_url (None | str | Unset): URL to the RSS feed, API endpoint, or hub URL (optional for system_level
            sources)
        is_enabled (bool | Unset): Whether this data source is active
        sync_interval_minutes (int | Unset): Interval in minutes between sync operations
        note_kind (str | Unset): Kind to assign to created notes (e.g., 'provider-status', 'news')
        note_organization_id (None | Unset | UUID):
        note_workspace_id (None | Unset | UUID):
        create_notes_resolved (bool | Unset): Whether to create notes with resolved=True (informational) or
            resolved=False (actionable)
        create_maintenance_as_draft (bool | Unset): Whether to create AI-detected maintenances as draft (default: True).
            Set to False to publish maintenances immediately and trigger notifications.
        create_incidents (bool | Unset): Whether to auto-create Incidents from provider-status outage events (default:
            True).
        create_incidents_without_resources (bool | Unset): Whether to create Incidents even when no Host/Volume was
            matched (default: True).
        last_sync (datetime.datetime | None | Unset): When the last sync was completed
        last_sync_error (None | str | Unset): Error message from last failed sync
        provider_entity_id (None | Unset | UUID):
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: DataSourceKindEnum | Unset = UNSET
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
    datasource_url: None | str | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    sync_interval_minutes: int | Unset = UNSET
    note_kind: str | Unset = UNSET
    note_organization_id: None | Unset | UUID = UNSET
    note_workspace_id: None | Unset | UUID = UNSET
    create_notes_resolved: bool | Unset = UNSET
    create_maintenance_as_draft: bool | Unset = UNSET
    create_incidents: bool | Unset = UNSET
    create_incidents_without_resources: bool | Unset = UNSET
    last_sync: datetime.datetime | None | Unset = UNSET
    last_sync_error: None | str | Unset = UNSET
    provider_entity_id: None | Unset | UUID = UNSET
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

        datasource_url: None | str | Unset
        if isinstance(self.datasource_url, Unset):
            datasource_url = UNSET
        else:
            datasource_url = self.datasource_url

        is_enabled = self.is_enabled

        sync_interval_minutes = self.sync_interval_minutes

        note_kind = self.note_kind

        note_organization_id: None | str | Unset
        if isinstance(self.note_organization_id, Unset):
            note_organization_id = UNSET
        elif isinstance(self.note_organization_id, UUID):
            note_organization_id = str(self.note_organization_id)
        else:
            note_organization_id = self.note_organization_id

        note_workspace_id: None | str | Unset
        if isinstance(self.note_workspace_id, Unset):
            note_workspace_id = UNSET
        elif isinstance(self.note_workspace_id, UUID):
            note_workspace_id = str(self.note_workspace_id)
        else:
            note_workspace_id = self.note_workspace_id

        create_notes_resolved = self.create_notes_resolved

        create_maintenance_as_draft = self.create_maintenance_as_draft

        create_incidents = self.create_incidents

        create_incidents_without_resources = self.create_incidents_without_resources

        last_sync: None | str | Unset
        if isinstance(self.last_sync, Unset):
            last_sync = UNSET
        elif isinstance(self.last_sync, datetime.datetime):
            last_sync = self.last_sync.isoformat()
        else:
            last_sync = self.last_sync

        last_sync_error: None | str | Unset
        if isinstance(self.last_sync_error, Unset):
            last_sync_error = UNSET
        else:
            last_sync_error = self.last_sync_error

        provider_entity_id: None | str | Unset
        if isinstance(self.provider_entity_id, Unset):
            provider_entity_id = UNSET
        elif isinstance(self.provider_entity_id, UUID):
            provider_entity_id = str(self.provider_entity_id)
        else:
            provider_entity_id = self.provider_entity_id

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
        if datasource_url is not UNSET:
            field_dict["datasource_url"] = datasource_url
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if sync_interval_minutes is not UNSET:
            field_dict["sync_interval_minutes"] = sync_interval_minutes
        if note_kind is not UNSET:
            field_dict["note_kind"] = note_kind
        if note_organization_id is not UNSET:
            field_dict["note_organization_id"] = note_organization_id
        if note_workspace_id is not UNSET:
            field_dict["note_workspace_id"] = note_workspace_id
        if create_notes_resolved is not UNSET:
            field_dict["create_notes_resolved"] = create_notes_resolved
        if create_maintenance_as_draft is not UNSET:
            field_dict["create_maintenance_as_draft"] = create_maintenance_as_draft
        if create_incidents is not UNSET:
            field_dict["create_incidents"] = create_incidents
        if create_incidents_without_resources is not UNSET:
            field_dict["create_incidents_without_resources"] = create_incidents_without_resources
        if last_sync is not UNSET:
            field_dict["last_sync"] = last_sync
        if last_sync_error is not UNSET:
            field_dict["last_sync_error"] = last_sync_error
        if provider_entity_id is not UNSET:
            field_dict["provider_entity_id"] = provider_entity_id

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

        if not isinstance(self.datasource_url, Unset):
            if isinstance(self.datasource_url, str):
                files.append(("datasource_url", (None, str(self.datasource_url).encode(), "text/plain")))
            else:
                files.append(("datasource_url", (None, str(self.datasource_url).encode(), "text/plain")))

        if not isinstance(self.is_enabled, Unset):
            files.append(("is_enabled", (None, str(self.is_enabled).encode(), "text/plain")))

        if not isinstance(self.sync_interval_minutes, Unset):
            files.append(("sync_interval_minutes", (None, str(self.sync_interval_minutes).encode(), "text/plain")))

        if not isinstance(self.note_kind, Unset):
            files.append(("note_kind", (None, str(self.note_kind).encode(), "text/plain")))

        if not isinstance(self.note_organization_id, Unset):
            if isinstance(self.note_organization_id, UUID):
                files.append(("note_organization_id", (None, str(self.note_organization_id), "text/plain")))
            else:
                files.append(("note_organization_id", (None, str(self.note_organization_id).encode(), "text/plain")))

        if not isinstance(self.note_workspace_id, Unset):
            if isinstance(self.note_workspace_id, UUID):
                files.append(("note_workspace_id", (None, str(self.note_workspace_id), "text/plain")))
            else:
                files.append(("note_workspace_id", (None, str(self.note_workspace_id).encode(), "text/plain")))

        if not isinstance(self.create_notes_resolved, Unset):
            files.append(("create_notes_resolved", (None, str(self.create_notes_resolved).encode(), "text/plain")))

        if not isinstance(self.create_maintenance_as_draft, Unset):
            files.append(
                ("create_maintenance_as_draft", (None, str(self.create_maintenance_as_draft).encode(), "text/plain"))
            )

        if not isinstance(self.create_incidents, Unset):
            files.append(("create_incidents", (None, str(self.create_incidents).encode(), "text/plain")))

        if not isinstance(self.create_incidents_without_resources, Unset):
            files.append(
                (
                    "create_incidents_without_resources",
                    (None, str(self.create_incidents_without_resources).encode(), "text/plain"),
                )
            )

        if not isinstance(self.last_sync, Unset):
            if isinstance(self.last_sync, datetime.datetime):
                files.append(("last_sync", (None, self.last_sync.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_sync", (None, str(self.last_sync).encode(), "text/plain")))

        if not isinstance(self.last_sync_error, Unset):
            if isinstance(self.last_sync_error, str):
                files.append(("last_sync_error", (None, str(self.last_sync_error).encode(), "text/plain")))
            else:
                files.append(("last_sync_error", (None, str(self.last_sync_error).encode(), "text/plain")))

        if not isinstance(self.provider_entity_id, Unset):
            if isinstance(self.provider_entity_id, UUID):
                files.append(("provider_entity_id", (None, str(self.provider_entity_id), "text/plain")))
            else:
                files.append(("provider_entity_id", (None, str(self.provider_entity_id).encode(), "text/plain")))

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
        kind: DataSourceKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_data_source_kind_enum(_kind)

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

        def _parse_datasource_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        datasource_url = _parse_datasource_url(d.pop("datasource_url", UNSET))

        is_enabled = d.pop("is_enabled", UNSET)

        sync_interval_minutes = d.pop("sync_interval_minutes", UNSET)

        note_kind = d.pop("note_kind", UNSET)

        def _parse_note_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                note_organization_id_type_0 = UUID(data)

                return note_organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        note_organization_id = _parse_note_organization_id(d.pop("note_organization_id", UNSET))

        def _parse_note_workspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                note_workspace_id_type_0 = UUID(data)

                return note_workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        note_workspace_id = _parse_note_workspace_id(d.pop("note_workspace_id", UNSET))

        create_notes_resolved = d.pop("create_notes_resolved", UNSET)

        create_maintenance_as_draft = d.pop("create_maintenance_as_draft", UNSET)

        create_incidents = d.pop("create_incidents", UNSET)

        create_incidents_without_resources = d.pop("create_incidents_without_resources", UNSET)

        def _parse_last_sync(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_type_0 = datetime.datetime.fromisoformat(data)

                return last_sync_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sync = _parse_last_sync(d.pop("last_sync", UNSET))

        def _parse_last_sync_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sync_error = _parse_last_sync_error(d.pop("last_sync_error", UNSET))

        def _parse_provider_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_entity_id_type_0 = UUID(data)

                return provider_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        provider_entity_id = _parse_provider_entity_id(d.pop("provider_entity_id", UNSET))

        data_source_request = cls(
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
            datasource_url=datasource_url,
            is_enabled=is_enabled,
            sync_interval_minutes=sync_interval_minutes,
            note_kind=note_kind,
            note_organization_id=note_organization_id,
            note_workspace_id=note_workspace_id,
            create_notes_resolved=create_notes_resolved,
            create_maintenance_as_draft=create_maintenance_as_draft,
            create_incidents=create_incidents,
            create_incidents_without_resources=create_incidents_without_resources,
            last_sync=last_sync,
            last_sync_error=last_sync_error,
            provider_entity_id=provider_entity_id,
        )

        data_source_request.additional_properties = d
        return data_source_request

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
