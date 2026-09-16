from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_config_request import RegionConfigRequest


T = TypeVar("T", bound="RegionRequest")


@_attrs_define
class RegionRequest:
    """Region Detail Serializer.
    Spec: polycrate spec inspect 309

    Writable fields: config, platform_features, platform_service (via ManagedObject)
    Read-only: workspace, legacy_s3_cluster, legacy_loadbalancer_region (auto-managed)

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
            state (LastStateEnum | Unset): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str | Unset):
            last_state (LastStateEnum | Unset): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            last_state_change (datetime.datetime | None | Unset):
            reconciliation_enabled (bool | Unset):
            reconciliation_running (bool | Unset):
            reconciliation_task_id (None | str | Unset):
            reconciliation_task_meta (Any | Unset): Task metadata for reconciliation progress tracking (e.g., step,
                progress, started_at)
            discovery_enabled (bool | Unset):
            discovery_running (bool | Unset):
            discovery_task_id (None | str | Unset):
            discovery_task_meta (Any | Unset): Task metadata for discovery progress tracking
            repair_running (bool | Unset):
            platform_service (bool | Unset): If True: managed by system owner org, available platform-wide to all
                organizations.
            repair_task_id (None | str | Unset):
            repair_task_meta (Any | Unset): Task metadata for repair progress tracking
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            conditions (Any | Unset): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
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
            actual_availability (str | Unset): Calculated actual availability as yearly average in %
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            platform_features (list[str] | Unset): Active platform services: 's3', 'loadbalancer', 'apm', 'dns',
                'controlplane'
            config (RegionConfigRequest | Unset):
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    state: LastStateEnum | Unset = UNSET
    state_reason: None | str | Unset = UNSET
    last_state: LastStateEnum | Unset = UNSET
    last_state_change: datetime.datetime | None | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    reconciliation_running: bool | Unset = UNSET
    reconciliation_task_id: None | str | Unset = UNSET
    reconciliation_task_meta: Any | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    discovery_running: bool | Unset = UNSET
    discovery_task_id: None | str | Unset = UNSET
    discovery_task_meta: Any | Unset = UNSET
    repair_running: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    repair_task_id: None | str | Unset = UNSET
    repair_task_meta: Any | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    conditions: Any | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    actual_availability: str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    platform_features: list[str] | Unset = UNSET
    config: RegionConfigRequest | Unset = UNSET
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

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        state_reason: None | str | Unset
        if isinstance(self.state_reason, Unset):
            state_reason = UNSET
        else:
            state_reason = self.state_reason

        last_state: str | Unset = UNSET
        if not isinstance(self.last_state, Unset):
            last_state = self.last_state

        last_state_change: None | str | Unset
        if isinstance(self.last_state_change, Unset):
            last_state_change = UNSET
        elif isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_enabled = self.reconciliation_enabled

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str | Unset
        if isinstance(self.reconciliation_task_id, Unset):
            reconciliation_task_id = UNSET
        else:
            reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        discovery_enabled = self.discovery_enabled

        discovery_running = self.discovery_running

        discovery_task_id: None | str | Unset
        if isinstance(self.discovery_task_id, Unset):
            discovery_task_id = UNSET
        else:
            discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        repair_running = self.repair_running

        platform_service = self.platform_service

        repair_task_id: None | str | Unset
        if isinstance(self.repair_task_id, Unset):
            repair_task_id = UNSET
        else:
            repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        conditions = self.conditions

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

        actual_availability = self.actual_availability

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

        platform_features: list[str] | Unset = UNSET
        if not isinstance(self.platform_features, Unset):
            platform_features = self.platform_features

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

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
        if state is not UNSET:
            field_dict["state"] = state
        if state_reason is not UNSET:
            field_dict["state_reason"] = state_reason
        if last_state is not UNSET:
            field_dict["last_state"] = last_state
        if last_state_change is not UNSET:
            field_dict["last_state_change"] = last_state_change
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if reconciliation_running is not UNSET:
            field_dict["reconciliation_running"] = reconciliation_running
        if reconciliation_task_id is not UNSET:
            field_dict["reconciliation_task_id"] = reconciliation_task_id
        if reconciliation_task_meta is not UNSET:
            field_dict["reconciliation_task_meta"] = reconciliation_task_meta
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if discovery_running is not UNSET:
            field_dict["discovery_running"] = discovery_running
        if discovery_task_id is not UNSET:
            field_dict["discovery_task_id"] = discovery_task_id
        if discovery_task_meta is not UNSET:
            field_dict["discovery_task_meta"] = discovery_task_meta
        if repair_running is not UNSET:
            field_dict["repair_running"] = repair_running
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if repair_task_id is not UNSET:
            field_dict["repair_task_id"] = repair_task_id
        if repair_task_meta is not UNSET:
            field_dict["repair_task_meta"] = repair_task_meta
        if scope is not UNSET:
            field_dict["scope"] = scope
        if kind is not UNSET:
            field_dict["kind"] = kind
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
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
        if actual_availability is not UNSET:
            field_dict["actual_availability"] = actual_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if platform_features is not UNSET:
            field_dict["platform_features"] = platform_features
        if config is not UNSET:
            field_dict["config"] = config

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

        if not isinstance(self.state, Unset):
            files.append(("state", (None, str(self.state).encode(), "text/plain")))

        if not isinstance(self.state_reason, Unset):
            if isinstance(self.state_reason, str):
                files.append(("state_reason", (None, str(self.state_reason).encode(), "text/plain")))
            else:
                files.append(("state_reason", (None, str(self.state_reason).encode(), "text/plain")))

        if not isinstance(self.last_state, Unset):
            files.append(("last_state", (None, str(self.last_state).encode(), "text/plain")))

        if not isinstance(self.last_state_change, Unset):
            if isinstance(self.last_state_change, datetime.datetime):
                files.append(("last_state_change", (None, self.last_state_change.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_state_change", (None, str(self.last_state_change).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.reconciliation_running, Unset):
            files.append(("reconciliation_running", (None, str(self.reconciliation_running).encode(), "text/plain")))

        if not isinstance(self.reconciliation_task_id, Unset):
            if isinstance(self.reconciliation_task_id, str):
                files.append(
                    ("reconciliation_task_id", (None, str(self.reconciliation_task_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("reconciliation_task_id", (None, str(self.reconciliation_task_id).encode(), "text/plain"))
                )

        if not isinstance(self.reconciliation_task_meta, Unset):
            files.append(
                ("reconciliation_task_meta", (None, str(self.reconciliation_task_meta).encode(), "text/plain"))
            )

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("discovery_enabled", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.discovery_running, Unset):
            files.append(("discovery_running", (None, str(self.discovery_running).encode(), "text/plain")))

        if not isinstance(self.discovery_task_id, Unset):
            if isinstance(self.discovery_task_id, str):
                files.append(("discovery_task_id", (None, str(self.discovery_task_id).encode(), "text/plain")))
            else:
                files.append(("discovery_task_id", (None, str(self.discovery_task_id).encode(), "text/plain")))

        if not isinstance(self.discovery_task_meta, Unset):
            files.append(("discovery_task_meta", (None, str(self.discovery_task_meta).encode(), "text/plain")))

        if not isinstance(self.repair_running, Unset):
            files.append(("repair_running", (None, str(self.repair_running).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.repair_task_id, Unset):
            if isinstance(self.repair_task_id, str):
                files.append(("repair_task_id", (None, str(self.repair_task_id).encode(), "text/plain")))
            else:
                files.append(("repair_task_id", (None, str(self.repair_task_id).encode(), "text/plain")))

        if not isinstance(self.repair_task_meta, Unset):
            files.append(("repair_task_meta", (None, str(self.repair_task_meta).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.conditions, Unset):
            files.append(("conditions", (None, str(self.conditions).encode(), "text/plain")))

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

        if not isinstance(self.actual_availability, Unset):
            files.append(("actual_availability", (None, str(self.actual_availability).encode(), "text/plain")))

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

        if not isinstance(self.platform_features, Unset):
            for platform_features_item_element in self.platform_features:
                files.append(("platform_features", (None, str(platform_features_item_element).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, json.dumps(self.config.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_config_request import RegionConfigRequest  # noqa: PLC0415

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

        _state = d.pop("state", UNSET)
        state: LastStateEnum | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_last_state_enum(_state)

        def _parse_state_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_reason = _parse_state_reason(d.pop("state_reason", UNSET))

        _last_state = d.pop("last_state", UNSET)
        last_state: LastStateEnum | Unset
        if isinstance(_last_state, Unset):
            last_state = UNSET
        else:
            last_state = check_last_state_enum(_last_state)

        def _parse_last_state_change(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        reconciliation_running = d.pop("reconciliation_running", UNSET)

        def _parse_reconciliation_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id", UNSET))

        reconciliation_task_meta = d.pop("reconciliation_task_meta", UNSET)

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        discovery_running = d.pop("discovery_running", UNSET)

        def _parse_discovery_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id", UNSET))

        discovery_task_meta = d.pop("discovery_task_meta", UNSET)

        repair_running = d.pop("repair_running", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        def _parse_repair_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id", UNSET))

        repair_task_meta = d.pop("repair_task_meta", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

        conditions = d.pop("conditions", UNSET)

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

        actual_availability = d.pop("actual_availability", UNSET)

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

        platform_features = cast(list[str], d.pop("platform_features", UNSET))

        _config = d.pop("config", UNSET)
        config: RegionConfigRequest | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = RegionConfigRequest.from_dict(_config)

        region_request = cls(
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_enabled=reconciliation_enabled,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            repair_running=repair_running,
            platform_service=platform_service,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            scope=scope,
            kind=kind,
            conditions=conditions,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            actual_availability=actual_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            platform_features=platform_features,
            config=config,
        )

        region_request.additional_properties = d
        return region_request

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
