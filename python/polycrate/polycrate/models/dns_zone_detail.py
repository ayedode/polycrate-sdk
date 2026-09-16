from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.dns_zone_kind_enum import DNSZoneKindEnum, check_dns_zone_kind_enum
from ..models.dnssec_algorithm_enum import DnssecAlgorithmEnum, check_dnssec_algorithm_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_simple import CredentialSimple
    from ..models.dns_zone_detail_created import DNSZoneDetailCreated
    from ..models.dns_zone_detail_deleted_by_user_type_0 import DNSZoneDetailDeletedByUserType0
    from ..models.dns_zone_detail_last_action_run_type_0 import DNSZoneDetailLastActionRunType0
    from ..models.dns_zone_detail_organization_type_0 import DNSZoneDetailOrganizationType0
    from ..models.dns_zone_detail_workspace_type_0 import DNSZoneDetailWorkspaceType0
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="DNSZoneDetail")


@_attrs_define
class DNSZoneDetail:
    """Basis-Serializer für alle ManagedObject Detail-Endpoints.

    Enthält alle generischen Felder eines ManagedObjects.
    Subclasses erweitern diese Liste mit model-spezifischen Feldern.

    Inkludiert:
    - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
    - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
    - organization/workspace als generische ManagedObject-Referenzen (mit URL)
    - created: Kombifeld (created_at, created_at_humanized, created_by)
    - url: Absolute URL zum Object (via get_absolute_url())

    Usage:
        class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
            class Meta(ManagedObjectDetailSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

        Attributes:
            id (UUID):
            created (DNSZoneDetailCreated):
            organization (DNSZoneDetailOrganizationType0 | None):
            workspace (DNSZoneDetailWorkspaceType0 | None):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            effective_criticality (EffectiveCriticalityEnum | None):
            last_action_run (DNSZoneDetailLastActionRunType0 | None):
            deleted_by_user (DNSZoneDetailDeletedByUserType0 | None):
            credential (CredentialSimple): Simple serializer for embedding Credential in other serializers.
            organization_id (UUID): UUID of the Organization this DNS zone belongs to. Required on create. Org API Key users
                can only set their own organization.
            sync_from_name (str):
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            computed_cost (float):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            last_state_change (datetime.datetime | None):
            reconciliation_running (bool):
            reconciliation_task_id (None | str):
            reconciliation_task_meta (Any): Task metadata for reconciliation progress tracking (e.g., step, progress,
                started_at)
            last_reconciliation (datetime.datetime | None):
            discovery_enabled (bool):
            discovery_running (bool):
            discovery_task_id (None | str):
            discovery_task_meta (Any): Task metadata for discovery progress tracking
            last_discovery (datetime.datetime | None):
            repair_running (bool):
            repair_task_id (None | str):
            repair_task_meta (Any): Task metadata for repair progress tracking
            last_repair (datetime.datetime | None):
            scope (ScopeEnum): * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            actual_availability (str): Calculated actual availability as yearly average in %
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider_reference (None | str | Unset):
            provider_id (None | str | Unset):
            reconciliation_enabled (bool | Unset):
            last_reconciliation_duration_seconds (float | None | Unset): Duration of the last reconciliation in seconds
            platform_service (bool | Unset):
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            created_by_component (BlankEnum | CreatedByComponentEnum | None | Unset): Component that created this object:
                cli, operator, or api.

                * `cli` - CLI
                * `operator` - Operator
                * `api` - API
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_window_days (int | None | Unset): SLO window in days. Null = use SystemConfig DEFAULT_SLO_WINDOW_DAYS
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_window_days (int | None | Unset): SLA window in days. Null = use SystemConfig DEFAULT_SLA_WINDOW_DAYS (365)
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            managed_by_object_id (None | str | Unset):
            platform_dns_record_created (bool | Unset):
            kind (DNSZoneKindEnum | Unset): * `internal` - Internal
                * `external` - External Default: 'internal'.
            provider (None | str | Unset): Lexicon provider name (e.g. 'cloudflare', 'hetzner', 'route53'). Required for
                kind='external'. Immutable after creation.
            primary_zone (bool | Unset): When multiple external DNS zones share the same name in an organization (different
                providers), the primary zone is preferred for DNS01/ACME and other single-writer automations. Default true.
                Default: True.
            powerdns_metadata (Any | Unset): Zone metadata as returned by the PowerDNS API (rrsets excluded).
            default_ttl (int | Unset): Default TTL (in seconds) applied to new DNS records in this zone.
            dnssec_enabled (bool | Unset): Whether DNSSEC is enabled for this zone (internal zones only).
            dnssec_algorithm (BlankEnum | DnssecAlgorithmEnum | Unset): DNSSEC signing algorithm. Only relevant when
                dnssec_enabled=True.

                * `ecdsa256` - ECDSA P-256 / SHA-256 (recommended)
                * `ecdsa384` - ECDSA P-384 / SHA-384
                * `ed25519` - Ed25519
                * `rsasha256` - RSA / SHA-256
            dnssec_nsec3 (bool | Unset): Use NSEC3 (hashed denial-of-existence) instead of plain NSEC. Recommended to
                prevent zone enumeration. Only relevant when dnssec_enabled=True.
            dnssec_ds_records (Any | Unset): DS records (public metadata) for delegation to a parent zone. Populated
                automatically when DNSSEC is enabled.
            dnssec_cryptokeys (Any | Unset): Public DNSSEC key metadata as returned by the PowerDNS API. Does NOT contain
                private key material.
            ns_delegation_synced (bool | Unset): NS records for this zone have been set in the parent zone.
            ds_delegation_synced (bool | Unset): DS records for this zone have been set in the parent zone.
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
            sync_from (None | Unset | UUID): Mirror DNS records from this zone. When set, all records are kept in sync with
                the source zone via the reconciliation loop (5-minute interval). Target must be kind='internal'; source may be
                internal or external. Must be in the same organization.
    """

    id: UUID
    created: DNSZoneDetailCreated
    organization: DNSZoneDetailOrganizationType0 | None
    workspace: DNSZoneDetailWorkspaceType0 | None
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    effective_criticality: EffectiveCriticalityEnum | None
    last_action_run: DNSZoneDetailLastActionRunType0 | None
    deleted_by_user: DNSZoneDetailDeletedByUserType0 | None
    credential: CredentialSimple
    organization_id: UUID
    sync_from_name: str
    product: ProductSimple
    computed_cost: float
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_running: bool
    reconciliation_task_id: None | str
    reconciliation_task_meta: Any
    last_reconciliation: datetime.datetime | None
    discovery_enabled: bool
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    scope: ScopeEnum
    conditions: Any
    actual_availability: str
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    platform_service: bool | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    kind: DNSZoneKindEnum | Unset = "internal"
    provider: None | str | Unset = UNSET
    primary_zone: bool | Unset = True
    powerdns_metadata: Any | Unset = UNSET
    default_ttl: int | Unset = UNSET
    dnssec_enabled: bool | Unset = UNSET
    dnssec_algorithm: BlankEnum | DnssecAlgorithmEnum | Unset = UNSET
    dnssec_nsec3: bool | Unset = UNSET
    dnssec_ds_records: Any | Unset = UNSET
    dnssec_cryptokeys: Any | Unset = UNSET
    ns_delegation_synced: bool | Unset = UNSET
    ds_delegation_synced: bool | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    sync_from: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dns_zone_detail_deleted_by_user_type_0 import DNSZoneDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.dns_zone_detail_last_action_run_type_0 import DNSZoneDetailLastActionRunType0  # noqa: PLC0415
        from ..models.dns_zone_detail_organization_type_0 import DNSZoneDetailOrganizationType0  # noqa: PLC0415
        from ..models.dns_zone_detail_workspace_type_0 import DNSZoneDetailWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        created = self.created.to_dict()

        organization: dict[str, Any] | None
        if isinstance(self.organization, DNSZoneDetailOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, DNSZoneDetailWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, DNSZoneDetailLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, DNSZoneDetailDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        credential = self.credential.to_dict()

        organization_id = str(self.organization_id)

        sync_from_name = self.sync_from_name

        product = self.product.to_dict()

        computed_cost = self.computed_cost

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        state: str = self.state

        state_reason: None | str
        state_reason = self.state_reason

        last_state: str = self.last_state

        last_state_change: None | str
        if isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str
        reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        last_reconciliation: None | str
        if isinstance(self.last_reconciliation, datetime.datetime):
            last_reconciliation = self.last_reconciliation.isoformat()
        else:
            last_reconciliation = self.last_reconciliation

        discovery_enabled = self.discovery_enabled

        discovery_running = self.discovery_running

        discovery_task_id: None | str
        discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        last_discovery: None | str
        if isinstance(self.last_discovery, datetime.datetime):
            last_discovery = self.last_discovery.isoformat()
        else:
            last_discovery = self.last_discovery

        repair_running = self.repair_running

        repair_task_id: None | str
        repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        scope: str = self.scope

        conditions = self.conditions

        actual_availability = self.actual_availability

        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        debug_mode = self.debug_mode

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

        last_reconciliation_duration_seconds: float | None | Unset
        if isinstance(self.last_reconciliation_duration_seconds, Unset):
            last_reconciliation_duration_seconds = UNSET
        else:
            last_reconciliation_duration_seconds = self.last_reconciliation_duration_seconds

        platform_service = self.platform_service

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

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        else:
            created_by_component = self.created_by_component

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

        slo_window_days: int | None | Unset
        if isinstance(self.slo_window_days, Unset):
            slo_window_days = UNSET
        else:
            slo_window_days = self.slo_window_days

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_window_days: int | None | Unset
        if isinstance(self.sla_window_days, Unset):
            sla_window_days = UNSET
        else:
            sla_window_days = self.sla_window_days

        sla_availability = self.sla_availability

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        managed_by_object_id: None | str | Unset
        if isinstance(self.managed_by_object_id, Unset):
            managed_by_object_id = UNSET
        else:
            managed_by_object_id = self.managed_by_object_id

        platform_dns_record_created = self.platform_dns_record_created

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        primary_zone = self.primary_zone

        powerdns_metadata = self.powerdns_metadata

        default_ttl = self.default_ttl

        dnssec_enabled = self.dnssec_enabled

        dnssec_algorithm: str | Unset
        if isinstance(self.dnssec_algorithm, Unset):
            dnssec_algorithm = UNSET
        elif isinstance(self.dnssec_algorithm, str):
            dnssec_algorithm = self.dnssec_algorithm
        else:
            dnssec_algorithm = self.dnssec_algorithm

        dnssec_nsec3 = self.dnssec_nsec3

        dnssec_ds_records = self.dnssec_ds_records

        dnssec_cryptokeys = self.dnssec_cryptokeys

        ns_delegation_synced = self.ns_delegation_synced

        ds_delegation_synced = self.ds_delegation_synced

        archived_by: int | None | Unset
        if isinstance(self.archived_by, Unset):
            archived_by = UNSET
        else:
            archived_by = self.archived_by

        managed_by_content_type: int | None | Unset
        if isinstance(self.managed_by_content_type, Unset):
            managed_by_content_type = UNSET
        else:
            managed_by_content_type = self.managed_by_content_type

        modified_by_user: int | None | Unset
        if isinstance(self.modified_by_user, Unset):
            modified_by_user = UNSET
        else:
            modified_by_user = self.modified_by_user

        created_by_user: int | None | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = self.created_by_user

        sync_from: None | str | Unset
        if isinstance(self.sync_from, Unset):
            sync_from = UNSET
        elif isinstance(self.sync_from, UUID):
            sync_from = str(self.sync_from)
        else:
            sync_from = self.sync_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "organization": organization,
                "workspace": workspace,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "effective_criticality": effective_criticality,
                "last_action_run": last_action_run,
                "deleted_by_user": deleted_by_user,
                "credential": credential,
                "organization_id": organization_id,
                "sync_from_name": sync_from_name,
                "product": product,
                "computed_cost": computed_cost,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_running": reconciliation_running,
                "reconciliation_task_id": reconciliation_task_id,
                "reconciliation_task_meta": reconciliation_task_meta,
                "last_reconciliation": last_reconciliation,
                "discovery_enabled": discovery_enabled,
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "scope": scope,
                "conditions": conditions,
                "actual_availability": actual_availability,
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
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if provider_reference is not UNSET:
            field_dict["provider_reference"] = provider_reference
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if last_reconciliation_duration_seconds is not UNSET:
            field_dict["last_reconciliation_duration_seconds"] = last_reconciliation_duration_seconds
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_window_days is not UNSET:
            field_dict["slo_window_days"] = slo_window_days
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_window_days is not UNSET:
            field_dict["sla_window_days"] = sla_window_days
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id
        if platform_dns_record_created is not UNSET:
            field_dict["platform_dns_record_created"] = platform_dns_record_created
        if kind is not UNSET:
            field_dict["kind"] = kind
        if provider is not UNSET:
            field_dict["provider"] = provider
        if primary_zone is not UNSET:
            field_dict["primary_zone"] = primary_zone
        if powerdns_metadata is not UNSET:
            field_dict["powerdns_metadata"] = powerdns_metadata
        if default_ttl is not UNSET:
            field_dict["default_ttl"] = default_ttl
        if dnssec_enabled is not UNSET:
            field_dict["dnssec_enabled"] = dnssec_enabled
        if dnssec_algorithm is not UNSET:
            field_dict["dnssec_algorithm"] = dnssec_algorithm
        if dnssec_nsec3 is not UNSET:
            field_dict["dnssec_nsec3"] = dnssec_nsec3
        if dnssec_ds_records is not UNSET:
            field_dict["dnssec_ds_records"] = dnssec_ds_records
        if dnssec_cryptokeys is not UNSET:
            field_dict["dnssec_cryptokeys"] = dnssec_cryptokeys
        if ns_delegation_synced is not UNSET:
            field_dict["ns_delegation_synced"] = ns_delegation_synced
        if ds_delegation_synced is not UNSET:
            field_dict["ds_delegation_synced"] = ds_delegation_synced
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if sync_from is not UNSET:
            field_dict["sync_from"] = sync_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_simple import CredentialSimple  # noqa: PLC0415
        from ..models.dns_zone_detail_created import DNSZoneDetailCreated  # noqa: PLC0415
        from ..models.dns_zone_detail_deleted_by_user_type_0 import DNSZoneDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.dns_zone_detail_last_action_run_type_0 import DNSZoneDetailLastActionRunType0  # noqa: PLC0415
        from ..models.dns_zone_detail_organization_type_0 import DNSZoneDetailOrganizationType0  # noqa: PLC0415
        from ..models.dns_zone_detail_workspace_type_0 import DNSZoneDetailWorkspaceType0  # noqa: PLC0415
        from ..models.product_simple import ProductSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = DNSZoneDetailCreated.from_dict(d.pop("created"))

        def _parse_organization(data: object) -> DNSZoneDetailOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = DNSZoneDetailOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneDetailOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> DNSZoneDetailWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = DNSZoneDetailWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneDetailWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        url = d.pop("url")

        icon_url = d.pop("icon_url")

        is_class_icon = d.pop("is_class_icon")

        def _parse_effective_slo_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_slo_target = _parse_effective_slo_target(d.pop("effective_slo_target"))

        def _parse_effective_sla_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_sla_target = _parse_effective_sla_target(d.pop("effective_sla_target"))

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

        def _parse_last_action_run(data: object) -> DNSZoneDetailLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = DNSZoneDetailLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneDetailLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_deleted_by_user(data: object) -> DNSZoneDetailDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = DNSZoneDetailDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DNSZoneDetailDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        credential = CredentialSimple.from_dict(d.pop("credential"))

        organization_id = UUID(d.pop("organization_id"))

        sync_from_name = d.pop("sync_from_name")

        product = ProductSimple.from_dict(d.pop("product"))

        computed_cost = d.pop("computed_cost")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        is_deleted = d.pop("is_deleted")

        state = check_last_state_enum(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_last_state_enum(d.pop("last_state"))

        def _parse_last_state_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change"))

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_reconciliation_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id"))

        reconciliation_task_meta = d.pop("reconciliation_task_meta")

        def _parse_last_reconciliation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reconciliation_type_0 = datetime.datetime.fromisoformat(data)

                return last_reconciliation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_reconciliation = _parse_last_reconciliation(d.pop("last_reconciliation"))

        discovery_enabled = d.pop("discovery_enabled")

        discovery_running = d.pop("discovery_running")

        def _parse_discovery_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id"))

        discovery_task_meta = d.pop("discovery_task_meta")

        def _parse_last_discovery(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_discovery_type_0 = datetime.datetime.fromisoformat(data)

                return last_discovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_discovery = _parse_last_discovery(d.pop("last_discovery"))

        repair_running = d.pop("repair_running")

        def _parse_repair_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id"))

        repair_task_meta = d.pop("repair_task_meta")

        def _parse_last_repair(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_repair_type_0 = datetime.datetime.fromisoformat(data)

                return last_repair_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_repair = _parse_last_repair(d.pop("last_repair"))

        scope = check_scope_enum(d.pop("scope"))

        conditions = d.pop("conditions")

        actual_availability = d.pop("actual_availability")

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

        def _parse_last_reconciliation_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_reconciliation_duration_seconds = _parse_last_reconciliation_duration_seconds(
            d.pop("last_reconciliation_duration_seconds", UNSET)
        )

        platform_service = d.pop("platform_service", UNSET)

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

        def _parse_created_by_component(data: object) -> BlankEnum | CreatedByComponentEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_0 = check_created_by_component_enum(data)

                return created_by_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_blank_enum(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CreatedByComponentEnum | None | Unset, data)

        created_by_component = _parse_created_by_component(d.pop("created_by_component", UNSET))

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

        def _parse_slo_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slo_window_days = _parse_slo_window_days(d.pop("slo_window_days", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        def _parse_sla_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sla_window_days = _parse_sla_window_days(d.pop("sla_window_days", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

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

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: DNSZoneKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_dns_zone_kind_enum(_kind)

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        primary_zone = d.pop("primary_zone", UNSET)

        powerdns_metadata = d.pop("powerdns_metadata", UNSET)

        default_ttl = d.pop("default_ttl", UNSET)

        dnssec_enabled = d.pop("dnssec_enabled", UNSET)

        def _parse_dnssec_algorithm(data: object) -> BlankEnum | DnssecAlgorithmEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dnssec_algorithm_type_0 = check_dnssec_algorithm_enum(data)

                return dnssec_algorithm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            dnssec_algorithm_type_1 = check_blank_enum(data)

            return dnssec_algorithm_type_1

        dnssec_algorithm = _parse_dnssec_algorithm(d.pop("dnssec_algorithm", UNSET))

        dnssec_nsec3 = d.pop("dnssec_nsec3", UNSET)

        dnssec_ds_records = d.pop("dnssec_ds_records", UNSET)

        dnssec_cryptokeys = d.pop("dnssec_cryptokeys", UNSET)

        ns_delegation_synced = d.pop("ns_delegation_synced", UNSET)

        ds_delegation_synced = d.pop("ds_delegation_synced", UNSET)

        def _parse_archived_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archived_by = _parse_archived_by(d.pop("archived_by", UNSET))

        def _parse_managed_by_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type", UNSET))

        def _parse_modified_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        modified_by_user = _parse_modified_by_user(d.pop("modified_by_user", UNSET))

        def _parse_created_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

        def _parse_sync_from(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sync_from_type_0 = UUID(data)

                return sync_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sync_from = _parse_sync_from(d.pop("sync_from", UNSET))

        dns_zone_detail = cls(
            id=id,
            created=created,
            organization=organization,
            workspace=workspace,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            effective_criticality=effective_criticality,
            last_action_run=last_action_run,
            deleted_by_user=deleted_by_user,
            credential=credential,
            organization_id=organization_id,
            sync_from_name=sync_from_name,
            product=product,
            computed_cost=computed_cost,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            last_reconciliation=last_reconciliation,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            scope=scope,
            conditions=conditions,
            actual_availability=actual_availability,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            platform_service=platform_service,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            created_by_component=created_by_component,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_window_days=slo_window_days,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_window_days=sla_window_days,
            sla_availability=sla_availability,
            criticality=criticality,
            managed_by_object_id=managed_by_object_id,
            platform_dns_record_created=platform_dns_record_created,
            kind=kind,
            provider=provider,
            primary_zone=primary_zone,
            powerdns_metadata=powerdns_metadata,
            default_ttl=default_ttl,
            dnssec_enabled=dnssec_enabled,
            dnssec_algorithm=dnssec_algorithm,
            dnssec_nsec3=dnssec_nsec3,
            dnssec_ds_records=dnssec_ds_records,
            dnssec_cryptokeys=dnssec_cryptokeys,
            ns_delegation_synced=ns_delegation_synced,
            ds_delegation_synced=ds_delegation_synced,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            sync_from=sync_from,
        )

        dns_zone_detail.additional_properties = d
        return dns_zone_detail

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
