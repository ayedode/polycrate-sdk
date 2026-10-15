from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pop_api_type import PopApiType, check_pop_api_type
from ..models.pop_bgp_status import PopBgpStatus, check_pop_bgp_status
from ..models.pop_byoip_status import PopByoipStatus, check_pop_byoip_status
from ..models.pop_c5_status import PopC5Status, check_pop_c5_status
from ..models.pop_colocation import PopColocation, check_pop_colocation
from ..models.pop_criticality_type_1 import PopCriticalityType1, check_pop_criticality_type_1
from ..models.pop_criticality_type_2_type_1 import PopCriticalityType2Type1, check_pop_criticality_type_2_type_1
from ..models.pop_criticality_type_3_type_1 import PopCriticalityType3Type1, check_pop_criticality_type_3_type_1
from ..models.pop_effective_criticality_type_1 import (
    PopEffectiveCriticalityType1,
    check_pop_effective_criticality_type_1,
)
from ..models.pop_effective_criticality_type_2_type_1 import (
    PopEffectiveCriticalityType2Type1,
    check_pop_effective_criticality_type_2_type_1,
)
from ..models.pop_effective_criticality_type_3_type_1 import (
    PopEffectiveCriticalityType3Type1,
    check_pop_effective_criticality_type_3_type_1,
)
from ..models.pop_en_50600_status import PopEn50600Status, check_pop_en_50600_status
from ..models.pop_ipv_6_status import PopIpv6Status, check_pop_ipv_6_status
from ..models.pop_iso_27001_status import PopIso27001Status, check_pop_iso_27001_status
from ..models.pop_kind import PopKind, check_pop_kind
from ..models.pop_last_state import PopLastState, check_pop_last_state
from ..models.pop_own_rz import PopOwnRz, check_pop_own_rz
from ..models.pop_provider import PopProvider, check_pop_provider
from ..models.pop_public_ipv_4_status import PopPublicIpv4Status, check_pop_public_ipv_4_status
from ..models.pop_scope import PopScope, check_pop_scope
from ..models.pop_scs_iaas_status import PopScsIaasStatus, check_pop_scs_iaas_status
from ..models.pop_scs_kaas_status import PopScsKaasStatus, check_pop_scs_kaas_status
from ..models.pop_state import PopState, check_pop_state
from ..models.pop_tier import PopTier, check_pop_tier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pop_created import PopCreated
    from ..models.pop_deleted_by_user_type_0 import PopDeletedByUserType0
    from ..models.pop_last_action_run_type_0 import PopLastActionRunType0
    from ..models.pop_organization_type_0 import PopOrganizationType0
    from ..models.pop_reachability_endpoint import PopReachabilityEndpoint
    from ..models.pop_workspace_type_0 import PopWorkspaceType0
    from ..models.provider_simple import ProviderSimple


T = TypeVar("T", bound="Pop")


@_attrs_define
class Pop:
    """Full serializer for Pop detail views.
    Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
    Pop is admin-only and not scoped to org/workspace.

    Spec 526 / 553:
    - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
    - reachability_endpoint: nested RO (managed ICMP endpoint)

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (None | PopDeletedByUserType0):
            state (PopState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (PopLastState): * `OK` - Ok
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
            scope (PopScope): The scope is used to separate `system` owned objects from `user` owned objects.

                * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            effective_criticality (None | PopEffectiveCriticalityType1 | PopEffectiveCriticalityType2Type1 |
                PopEffectiveCriticalityType3Type1):
            actual_availability (str): Calculated actual availability as yearly average in %
            organization (None | PopOrganizationType0):
            workspace (None | PopWorkspaceType0):
            created (PopCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (None | PopLastActionRunType0):
            provider_entity (ProviderSimple): Compact serializer for embedding Provider in other serializers (FK/M2M).
            reachability_endpoint (PopReachabilityEndpoint): Read-only nested reachability endpoint for Pop detail (Spec
                526).
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (PopProvider | Unset): * `loopback` - Loopback
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
            kind (PopKind | Unset): * `datacenter` - Datacenter
                * `datacenter-park` - Datacenter Park
                * `region` - Region
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (None | PopCriticalityType1 | PopCriticalityType2Type1 | PopCriticalityType3Type1 | Unset):
                Criticality level. Null = inherit from workspace, then org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            region (None | str | Unset): Broader region identifier (e.g., 'Europe', 'North America')
            country (None | str | Unset): ISO 3166-1 alpha-2 country code
            city (None | str | Unset): City where the PoP is located
            description (None | str | Unset):
            latitude (None | str | Unset): Latitude coordinate
            longitude (None | str | Unset): Longitude coordinate
            pop_endpoint_remote_address (None | str | Unset): Router/gateway IP or hostname for PoP reachability ICMP
                monitoring (Spec 526).
            iso27001_status (PopIso27001Status | Unset): ISO 27001 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (PopC5Status | Unset): BSI C5 status for this PoP.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            tier (PopTier | Unset): Site tier. EN 50600 is a separate field.

                * `tier1` - Tier 1
                * `tier2` - Tier 2
                * `tier3` - Tier 3
                * `tier4` - Tier 4
            en50600_status (PopEn50600Status | Unset): EN 50600 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (PopScsIaasStatus | Unset): SCS-compatible IaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (PopScsKaasStatus | Unset): SCS-compatible KaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            technologies (Any | Unset): Hypervisors at this PoP: openstack, proxmox, custom, other.
            api_type (PopApiType | Unset): Primary API at this PoP.

                * `openstack` - OpenStack
                * `proxmox` - Proxmox
                * `custom_rest` - Custom REST
                * `none` - None
            public_ipv4_status (PopPublicIpv4Status | Unset): Public IPv4 at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            ipv6_status (PopIpv6Status | Unset): IPv6 at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            bgp_status (PopBgpStatus | Unset): BGP at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            byoip_status (PopByoipStatus | Unset): BYOIP at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            own_rz (PopOwnRz | Unset): Provider-owned data center at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            colocation (PopColocation | Unset): Colocation at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            certification_evidence (Any | Unset): HTTPS evidence URLs, e.g. [{"claim": "tier", "url": "https://..."}].
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: None | PopDeletedByUserType0
    state: PopState
    state_reason: None | str
    last_state: PopLastState
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
    scope: PopScope
    conditions: Any
    effective_criticality: (
        None | PopEffectiveCriticalityType1 | PopEffectiveCriticalityType2Type1 | PopEffectiveCriticalityType3Type1
    )
    actual_availability: str
    organization: None | PopOrganizationType0
    workspace: None | PopWorkspaceType0
    created: PopCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: None | PopLastActionRunType0
    provider_entity: ProviderSimple
    reachability_endpoint: PopReachabilityEndpoint
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: PopProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: PopKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: None | PopCriticalityType1 | PopCriticalityType2Type1 | PopCriticalityType3Type1 | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    region: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    pop_endpoint_remote_address: None | str | Unset = UNSET
    iso27001_status: PopIso27001Status | Unset = UNSET
    c5_status: PopC5Status | Unset = UNSET
    tier: PopTier | Unset = UNSET
    en50600_status: PopEn50600Status | Unset = UNSET
    scs_iaas_status: PopScsIaasStatus | Unset = UNSET
    scs_kaas_status: PopScsKaasStatus | Unset = UNSET
    technologies: Any | Unset = UNSET
    api_type: PopApiType | Unset = UNSET
    public_ipv4_status: PopPublicIpv4Status | Unset = UNSET
    ipv6_status: PopIpv6Status | Unset = UNSET
    bgp_status: PopBgpStatus | Unset = UNSET
    byoip_status: PopByoipStatus | Unset = UNSET
    own_rz: PopOwnRz | Unset = UNSET
    colocation: PopColocation | Unset = UNSET
    certification_evidence: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pop_deleted_by_user_type_0 import PopDeletedByUserType0  # noqa: PLC0415
        from ..models.pop_last_action_run_type_0 import PopLastActionRunType0  # noqa: PLC0415
        from ..models.pop_organization_type_0 import PopOrganizationType0  # noqa: PLC0415
        from ..models.pop_workspace_type_0 import PopWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, PopDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

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

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        actual_availability = self.actual_availability

        organization: dict[str, Any] | None
        if isinstance(self.organization, PopOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, PopWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, PopLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        provider_entity = self.provider_entity.to_dict()

        reachability_endpoint = self.reachability_endpoint.to_dict()

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

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        pop_endpoint_remote_address: None | str | Unset
        if isinstance(self.pop_endpoint_remote_address, Unset):
            pop_endpoint_remote_address = UNSET
        else:
            pop_endpoint_remote_address = self.pop_endpoint_remote_address

        iso27001_status: str | Unset = UNSET
        if not isinstance(self.iso27001_status, Unset):
            iso27001_status = self.iso27001_status

        c5_status: str | Unset = UNSET
        if not isinstance(self.c5_status, Unset):
            c5_status = self.c5_status

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier

        en50600_status: str | Unset = UNSET
        if not isinstance(self.en50600_status, Unset):
            en50600_status = self.en50600_status

        scs_iaas_status: str | Unset = UNSET
        if not isinstance(self.scs_iaas_status, Unset):
            scs_iaas_status = self.scs_iaas_status

        scs_kaas_status: str | Unset = UNSET
        if not isinstance(self.scs_kaas_status, Unset):
            scs_kaas_status = self.scs_kaas_status

        technologies = self.technologies

        api_type: str | Unset = UNSET
        if not isinstance(self.api_type, Unset):
            api_type = self.api_type

        public_ipv4_status: str | Unset = UNSET
        if not isinstance(self.public_ipv4_status, Unset):
            public_ipv4_status = self.public_ipv4_status

        ipv6_status: str | Unset = UNSET
        if not isinstance(self.ipv6_status, Unset):
            ipv6_status = self.ipv6_status

        bgp_status: str | Unset = UNSET
        if not isinstance(self.bgp_status, Unset):
            bgp_status = self.bgp_status

        byoip_status: str | Unset = UNSET
        if not isinstance(self.byoip_status, Unset):
            byoip_status = self.byoip_status

        own_rz: str | Unset = UNSET
        if not isinstance(self.own_rz, Unset):
            own_rz = self.own_rz

        colocation: str | Unset = UNSET
        if not isinstance(self.colocation, Unset):
            colocation = self.colocation

        certification_evidence = self.certification_evidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "deleted_by_user": deleted_by_user,
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
                "effective_criticality": effective_criticality,
                "actual_availability": actual_availability,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "provider_entity": provider_entity,
                "reachability_endpoint": reachability_endpoint,
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
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city
        if description is not UNSET:
            field_dict["description"] = description
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if pop_endpoint_remote_address is not UNSET:
            field_dict["pop_endpoint_remote_address"] = pop_endpoint_remote_address
        if iso27001_status is not UNSET:
            field_dict["iso27001_status"] = iso27001_status
        if c5_status is not UNSET:
            field_dict["c5_status"] = c5_status
        if tier is not UNSET:
            field_dict["tier"] = tier
        if en50600_status is not UNSET:
            field_dict["en50600_status"] = en50600_status
        if scs_iaas_status is not UNSET:
            field_dict["scs_iaas_status"] = scs_iaas_status
        if scs_kaas_status is not UNSET:
            field_dict["scs_kaas_status"] = scs_kaas_status
        if technologies is not UNSET:
            field_dict["technologies"] = technologies
        if api_type is not UNSET:
            field_dict["api_type"] = api_type
        if public_ipv4_status is not UNSET:
            field_dict["public_ipv4_status"] = public_ipv4_status
        if ipv6_status is not UNSET:
            field_dict["ipv6_status"] = ipv6_status
        if bgp_status is not UNSET:
            field_dict["bgp_status"] = bgp_status
        if byoip_status is not UNSET:
            field_dict["byoip_status"] = byoip_status
        if own_rz is not UNSET:
            field_dict["own_rz"] = own_rz
        if colocation is not UNSET:
            field_dict["colocation"] = colocation
        if certification_evidence is not UNSET:
            field_dict["certification_evidence"] = certification_evidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pop_created import PopCreated  # noqa: PLC0415
        from ..models.pop_deleted_by_user_type_0 import PopDeletedByUserType0  # noqa: PLC0415
        from ..models.pop_last_action_run_type_0 import PopLastActionRunType0  # noqa: PLC0415
        from ..models.pop_organization_type_0 import PopOrganizationType0  # noqa: PLC0415
        from ..models.pop_reachability_endpoint import PopReachabilityEndpoint  # noqa: PLC0415
        from ..models.pop_workspace_type_0 import PopWorkspaceType0  # noqa: PLC0415
        from ..models.provider_simple import ProviderSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

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

        def _parse_deleted_by_user(data: object) -> None | PopDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = PopDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopDeletedByUserType0, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        state = check_pop_state(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_pop_last_state(d.pop("last_state"))

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

        scope = check_pop_scope(d.pop("scope"))

        conditions = d.pop("conditions")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            None | PopEffectiveCriticalityType1 | PopEffectiveCriticalityType2Type1 | PopEffectiveCriticalityType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_pop_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_pop_effective_criticality_type_2_type_1(data)

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_pop_effective_criticality_type_3_type_1(data)

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PopEffectiveCriticalityType1
                | PopEffectiveCriticalityType2Type1
                | PopEffectiveCriticalityType3Type1,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        actual_availability = d.pop("actual_availability")

        def _parse_organization(data: object) -> None | PopOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = PopOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> None | PopWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = PopWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = PopCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> None | PopLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = PopLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        provider_entity = ProviderSimple.from_dict(d.pop("provider_entity"))

        reachability_endpoint = PopReachabilityEndpoint.from_dict(d.pop("reachability_endpoint"))

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
        provider: PopProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_pop_provider(_provider)

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
        kind: PopKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_pop_kind(_kind)

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

        def _parse_criticality(
            data: object,
        ) -> None | PopCriticalityType1 | PopCriticalityType2Type1 | PopCriticalityType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_pop_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_pop_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_pop_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PopCriticalityType1 | PopCriticalityType2Type1 | PopCriticalityType3Type1 | Unset, data)

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

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_pop_endpoint_remote_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pop_endpoint_remote_address = _parse_pop_endpoint_remote_address(d.pop("pop_endpoint_remote_address", UNSET))

        _iso27001_status = d.pop("iso27001_status", UNSET)
        iso27001_status: PopIso27001Status | Unset
        if isinstance(_iso27001_status, Unset):
            iso27001_status = UNSET
        else:
            iso27001_status = check_pop_iso_27001_status(_iso27001_status)

        _c5_status = d.pop("c5_status", UNSET)
        c5_status: PopC5Status | Unset
        if isinstance(_c5_status, Unset):
            c5_status = UNSET
        else:
            c5_status = check_pop_c5_status(_c5_status)

        _tier = d.pop("tier", UNSET)
        tier: PopTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = check_pop_tier(_tier)

        _en50600_status = d.pop("en50600_status", UNSET)
        en50600_status: PopEn50600Status | Unset
        if isinstance(_en50600_status, Unset):
            en50600_status = UNSET
        else:
            en50600_status = check_pop_en_50600_status(_en50600_status)

        _scs_iaas_status = d.pop("scs_iaas_status", UNSET)
        scs_iaas_status: PopScsIaasStatus | Unset
        if isinstance(_scs_iaas_status, Unset):
            scs_iaas_status = UNSET
        else:
            scs_iaas_status = check_pop_scs_iaas_status(_scs_iaas_status)

        _scs_kaas_status = d.pop("scs_kaas_status", UNSET)
        scs_kaas_status: PopScsKaasStatus | Unset
        if isinstance(_scs_kaas_status, Unset):
            scs_kaas_status = UNSET
        else:
            scs_kaas_status = check_pop_scs_kaas_status(_scs_kaas_status)

        technologies = d.pop("technologies", UNSET)

        _api_type = d.pop("api_type", UNSET)
        api_type: PopApiType | Unset
        if isinstance(_api_type, Unset):
            api_type = UNSET
        else:
            api_type = check_pop_api_type(_api_type)

        _public_ipv4_status = d.pop("public_ipv4_status", UNSET)
        public_ipv4_status: PopPublicIpv4Status | Unset
        if isinstance(_public_ipv4_status, Unset):
            public_ipv4_status = UNSET
        else:
            public_ipv4_status = check_pop_public_ipv_4_status(_public_ipv4_status)

        _ipv6_status = d.pop("ipv6_status", UNSET)
        ipv6_status: PopIpv6Status | Unset
        if isinstance(_ipv6_status, Unset):
            ipv6_status = UNSET
        else:
            ipv6_status = check_pop_ipv_6_status(_ipv6_status)

        _bgp_status = d.pop("bgp_status", UNSET)
        bgp_status: PopBgpStatus | Unset
        if isinstance(_bgp_status, Unset):
            bgp_status = UNSET
        else:
            bgp_status = check_pop_bgp_status(_bgp_status)

        _byoip_status = d.pop("byoip_status", UNSET)
        byoip_status: PopByoipStatus | Unset
        if isinstance(_byoip_status, Unset):
            byoip_status = UNSET
        else:
            byoip_status = check_pop_byoip_status(_byoip_status)

        _own_rz = d.pop("own_rz", UNSET)
        own_rz: PopOwnRz | Unset
        if isinstance(_own_rz, Unset):
            own_rz = UNSET
        else:
            own_rz = check_pop_own_rz(_own_rz)

        _colocation = d.pop("colocation", UNSET)
        colocation: PopColocation | Unset
        if isinstance(_colocation, Unset):
            colocation = UNSET
        else:
            colocation = check_pop_colocation(_colocation)

        certification_evidence = d.pop("certification_evidence", UNSET)

        pop = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            deleted_by_user=deleted_by_user,
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
            effective_criticality=effective_criticality,
            actual_availability=actual_availability,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            provider_entity=provider_entity,
            reachability_endpoint=reachability_endpoint,
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
            region=region,
            country=country,
            city=city,
            description=description,
            latitude=latitude,
            longitude=longitude,
            pop_endpoint_remote_address=pop_endpoint_remote_address,
            iso27001_status=iso27001_status,
            c5_status=c5_status,
            tier=tier,
            en50600_status=en50600_status,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
            technologies=technologies,
            api_type=api_type,
            public_ipv4_status=public_ipv4_status,
            ipv6_status=ipv6_status,
            bgp_status=bgp_status,
            byoip_status=byoip_status,
            own_rz=own_rz,
            colocation=colocation,
            certification_evidence=certification_evidence,
        )

        pop.additional_properties = d
        return pop

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
