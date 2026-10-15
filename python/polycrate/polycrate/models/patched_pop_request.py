from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.patched_pop_request_api_type import PatchedPopRequestApiType, check_patched_pop_request_api_type
from ..models.patched_pop_request_bgp_status import PatchedPopRequestBgpStatus, check_patched_pop_request_bgp_status
from ..models.patched_pop_request_byoip_status import (
    PatchedPopRequestByoipStatus,
    check_patched_pop_request_byoip_status,
)
from ..models.patched_pop_request_c5_status import PatchedPopRequestC5Status, check_patched_pop_request_c5_status
from ..models.patched_pop_request_colocation import PatchedPopRequestColocation, check_patched_pop_request_colocation
from ..models.patched_pop_request_criticality_type_1 import (
    PatchedPopRequestCriticalityType1,
    check_patched_pop_request_criticality_type_1,
)
from ..models.patched_pop_request_criticality_type_2_type_1 import (
    PatchedPopRequestCriticalityType2Type1,
    check_patched_pop_request_criticality_type_2_type_1,
)
from ..models.patched_pop_request_criticality_type_3_type_1 import (
    PatchedPopRequestCriticalityType3Type1,
    check_patched_pop_request_criticality_type_3_type_1,
)
from ..models.patched_pop_request_en_50600_status import (
    PatchedPopRequestEn50600Status,
    check_patched_pop_request_en_50600_status,
)
from ..models.patched_pop_request_ipv_6_status import (
    PatchedPopRequestIpv6Status,
    check_patched_pop_request_ipv_6_status,
)
from ..models.patched_pop_request_iso_27001_status import (
    PatchedPopRequestIso27001Status,
    check_patched_pop_request_iso_27001_status,
)
from ..models.patched_pop_request_kind import PatchedPopRequestKind, check_patched_pop_request_kind
from ..models.patched_pop_request_own_rz import PatchedPopRequestOwnRz, check_patched_pop_request_own_rz
from ..models.patched_pop_request_provider import PatchedPopRequestProvider, check_patched_pop_request_provider
from ..models.patched_pop_request_public_ipv_4_status import (
    PatchedPopRequestPublicIpv4Status,
    check_patched_pop_request_public_ipv_4_status,
)
from ..models.patched_pop_request_scs_iaas_status import (
    PatchedPopRequestScsIaasStatus,
    check_patched_pop_request_scs_iaas_status,
)
from ..models.patched_pop_request_scs_kaas_status import (
    PatchedPopRequestScsKaasStatus,
    check_patched_pop_request_scs_kaas_status,
)
from ..models.patched_pop_request_tier import PatchedPopRequestTier, check_patched_pop_request_tier
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPopRequest")


@_attrs_define
class PatchedPopRequest:
    """Full serializer for Pop detail views.
    Per .specs/0.11.4/dynamic-table-v2.md - inherits from ManagedObjectDetailSerializer.
    Pop is admin-only and not scoped to org/workspace.

    Spec 526 / 553:
    - pop_endpoint_remote_address: RW (IP or hostname for PoP reachability ICMP)
    - reachability_endpoint: nested RO (managed ICMP endpoint)

        Attributes:
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (PatchedPopRequestProvider | Unset): * `loopback` - Loopback
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
            kind (PatchedPopRequestKind | Unset): * `datacenter` - Datacenter
                * `datacenter-park` - Datacenter Park
                * `region` - Region
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (None | PatchedPopRequestCriticalityType1 | PatchedPopRequestCriticalityType2Type1 |
                PatchedPopRequestCriticalityType3Type1 | Unset): Criticality level. Null = inherit from workspace, then org.
                Explicit value overrides inheritance.

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
            provider_entity_id (UUID | Unset):
            pop_endpoint_remote_address (None | str | Unset): Router/gateway IP or hostname for PoP reachability ICMP
                monitoring (Spec 526).
            iso27001_status (PatchedPopRequestIso27001Status | Unset): ISO 27001 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (PatchedPopRequestC5Status | Unset): BSI C5 status for this PoP.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            tier (PatchedPopRequestTier | Unset): Site tier. EN 50600 is a separate field.

                * `tier1` - Tier 1
                * `tier2` - Tier 2
                * `tier3` - Tier 3
                * `tier4` - Tier 4
            en50600_status (PatchedPopRequestEn50600Status | Unset): EN 50600 status for this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (PatchedPopRequestScsIaasStatus | Unset): SCS-compatible IaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (PatchedPopRequestScsKaasStatus | Unset): SCS-compatible KaaS status for this PoP.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            technologies (Any | Unset): Hypervisors at this PoP: openstack, proxmox, custom, other.
            api_type (PatchedPopRequestApiType | Unset): Primary API at this PoP.

                * `openstack` - OpenStack
                * `proxmox` - Proxmox
                * `custom_rest` - Custom REST
                * `none` - None
            public_ipv4_status (PatchedPopRequestPublicIpv4Status | Unset): Public IPv4 at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            ipv6_status (PatchedPopRequestIpv6Status | Unset): IPv6 at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            bgp_status (PatchedPopRequestBgpStatus | Unset): BGP at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            byoip_status (PatchedPopRequestByoipStatus | Unset): BYOIP at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            own_rz (PatchedPopRequestOwnRz | Unset): Provider-owned data center at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            colocation (PatchedPopRequestColocation | Unset): Colocation at this PoP.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            certification_evidence (Any | Unset): HTTPS evidence URLs, e.g. [{"claim": "tier", "url": "https://..."}].
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: PatchedPopRequestProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: PatchedPopRequestKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: (
        None
        | PatchedPopRequestCriticalityType1
        | PatchedPopRequestCriticalityType2Type1
        | PatchedPopRequestCriticalityType3Type1
        | Unset
    ) = UNSET
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
    provider_entity_id: UUID | Unset = UNSET
    pop_endpoint_remote_address: None | str | Unset = UNSET
    iso27001_status: PatchedPopRequestIso27001Status | Unset = UNSET
    c5_status: PatchedPopRequestC5Status | Unset = UNSET
    tier: PatchedPopRequestTier | Unset = UNSET
    en50600_status: PatchedPopRequestEn50600Status | Unset = UNSET
    scs_iaas_status: PatchedPopRequestScsIaasStatus | Unset = UNSET
    scs_kaas_status: PatchedPopRequestScsKaasStatus | Unset = UNSET
    technologies: Any | Unset = UNSET
    api_type: PatchedPopRequestApiType | Unset = UNSET
    public_ipv4_status: PatchedPopRequestPublicIpv4Status | Unset = UNSET
    ipv6_status: PatchedPopRequestIpv6Status | Unset = UNSET
    bgp_status: PatchedPopRequestBgpStatus | Unset = UNSET
    byoip_status: PatchedPopRequestByoipStatus | Unset = UNSET
    own_rz: PatchedPopRequestOwnRz | Unset = UNSET
    colocation: PatchedPopRequestColocation | Unset = UNSET
    certification_evidence: Any | Unset = UNSET
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

        provider_entity_id: str | Unset = UNSET
        if not isinstance(self.provider_entity_id, Unset):
            provider_entity_id = str(self.provider_entity_id)

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
        if provider_entity_id is not UNSET:
            field_dict["provider_entity_id"] = provider_entity_id
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
            if self.criticality is None:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
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

        if not isinstance(self.region, Unset):
            if isinstance(self.region, str):
                files.append(("region", (None, str(self.region).encode(), "text/plain")))
            else:
                files.append(("region", (None, str(self.region).encode(), "text/plain")))

        if not isinstance(self.country, Unset):
            if isinstance(self.country, str):
                files.append(("country", (None, str(self.country).encode(), "text/plain")))
            else:
                files.append(("country", (None, str(self.country).encode(), "text/plain")))

        if not isinstance(self.city, Unset):
            if isinstance(self.city, str):
                files.append(("city", (None, str(self.city).encode(), "text/plain")))
            else:
                files.append(("city", (None, str(self.city).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.latitude, Unset):
            if isinstance(self.latitude, str):
                files.append(("latitude", (None, str(self.latitude).encode(), "text/plain")))
            else:
                files.append(("latitude", (None, str(self.latitude).encode(), "text/plain")))

        if not isinstance(self.longitude, Unset):
            if isinstance(self.longitude, str):
                files.append(("longitude", (None, str(self.longitude).encode(), "text/plain")))
            else:
                files.append(("longitude", (None, str(self.longitude).encode(), "text/plain")))

        if not isinstance(self.provider_entity_id, Unset):
            files.append(("provider_entity_id", (None, str(self.provider_entity_id), "text/plain")))

        if not isinstance(self.pop_endpoint_remote_address, Unset):
            if isinstance(self.pop_endpoint_remote_address, str):
                files.append(
                    (
                        "pop_endpoint_remote_address",
                        (None, str(self.pop_endpoint_remote_address).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "pop_endpoint_remote_address",
                        (None, str(self.pop_endpoint_remote_address).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.iso27001_status, Unset):
            files.append(("iso27001_status", (None, str(self.iso27001_status).encode(), "text/plain")))

        if not isinstance(self.c5_status, Unset):
            files.append(("c5_status", (None, str(self.c5_status).encode(), "text/plain")))

        if not isinstance(self.tier, Unset):
            files.append(("tier", (None, str(self.tier).encode(), "text/plain")))

        if not isinstance(self.en50600_status, Unset):
            files.append(("en50600_status", (None, str(self.en50600_status).encode(), "text/plain")))

        if not isinstance(self.scs_iaas_status, Unset):
            files.append(("scs_iaas_status", (None, str(self.scs_iaas_status).encode(), "text/plain")))

        if not isinstance(self.scs_kaas_status, Unset):
            files.append(("scs_kaas_status", (None, str(self.scs_kaas_status).encode(), "text/plain")))

        if not isinstance(self.technologies, Unset):
            files.append(("technologies", (None, str(self.technologies).encode(), "text/plain")))

        if not isinstance(self.api_type, Unset):
            files.append(("api_type", (None, str(self.api_type).encode(), "text/plain")))

        if not isinstance(self.public_ipv4_status, Unset):
            files.append(("public_ipv4_status", (None, str(self.public_ipv4_status).encode(), "text/plain")))

        if not isinstance(self.ipv6_status, Unset):
            files.append(("ipv6_status", (None, str(self.ipv6_status).encode(), "text/plain")))

        if not isinstance(self.bgp_status, Unset):
            files.append(("bgp_status", (None, str(self.bgp_status).encode(), "text/plain")))

        if not isinstance(self.byoip_status, Unset):
            files.append(("byoip_status", (None, str(self.byoip_status).encode(), "text/plain")))

        if not isinstance(self.own_rz, Unset):
            files.append(("own_rz", (None, str(self.own_rz).encode(), "text/plain")))

        if not isinstance(self.colocation, Unset):
            files.append(("colocation", (None, str(self.colocation).encode(), "text/plain")))

        if not isinstance(self.certification_evidence, Unset):
            files.append(("certification_evidence", (None, str(self.certification_evidence).encode(), "text/plain")))

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
        provider: PatchedPopRequestProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_patched_pop_request_provider(_provider)

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
        kind: PatchedPopRequestKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_patched_pop_request_kind(_kind)

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
        ) -> (
            None
            | PatchedPopRequestCriticalityType1
            | PatchedPopRequestCriticalityType2Type1
            | PatchedPopRequestCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_patched_pop_request_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_patched_pop_request_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_patched_pop_request_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | PatchedPopRequestCriticalityType1
                | PatchedPopRequestCriticalityType2Type1
                | PatchedPopRequestCriticalityType3Type1
                | Unset,
                data,
            )

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

        _provider_entity_id = d.pop("provider_entity_id", UNSET)
        provider_entity_id: UUID | Unset
        if isinstance(_provider_entity_id, Unset):
            provider_entity_id = UNSET
        else:
            provider_entity_id = UUID(_provider_entity_id)

        def _parse_pop_endpoint_remote_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pop_endpoint_remote_address = _parse_pop_endpoint_remote_address(d.pop("pop_endpoint_remote_address", UNSET))

        _iso27001_status = d.pop("iso27001_status", UNSET)
        iso27001_status: PatchedPopRequestIso27001Status | Unset
        if isinstance(_iso27001_status, Unset):
            iso27001_status = UNSET
        else:
            iso27001_status = check_patched_pop_request_iso_27001_status(_iso27001_status)

        _c5_status = d.pop("c5_status", UNSET)
        c5_status: PatchedPopRequestC5Status | Unset
        if isinstance(_c5_status, Unset):
            c5_status = UNSET
        else:
            c5_status = check_patched_pop_request_c5_status(_c5_status)

        _tier = d.pop("tier", UNSET)
        tier: PatchedPopRequestTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = check_patched_pop_request_tier(_tier)

        _en50600_status = d.pop("en50600_status", UNSET)
        en50600_status: PatchedPopRequestEn50600Status | Unset
        if isinstance(_en50600_status, Unset):
            en50600_status = UNSET
        else:
            en50600_status = check_patched_pop_request_en_50600_status(_en50600_status)

        _scs_iaas_status = d.pop("scs_iaas_status", UNSET)
        scs_iaas_status: PatchedPopRequestScsIaasStatus | Unset
        if isinstance(_scs_iaas_status, Unset):
            scs_iaas_status = UNSET
        else:
            scs_iaas_status = check_patched_pop_request_scs_iaas_status(_scs_iaas_status)

        _scs_kaas_status = d.pop("scs_kaas_status", UNSET)
        scs_kaas_status: PatchedPopRequestScsKaasStatus | Unset
        if isinstance(_scs_kaas_status, Unset):
            scs_kaas_status = UNSET
        else:
            scs_kaas_status = check_patched_pop_request_scs_kaas_status(_scs_kaas_status)

        technologies = d.pop("technologies", UNSET)

        _api_type = d.pop("api_type", UNSET)
        api_type: PatchedPopRequestApiType | Unset
        if isinstance(_api_type, Unset):
            api_type = UNSET
        else:
            api_type = check_patched_pop_request_api_type(_api_type)

        _public_ipv4_status = d.pop("public_ipv4_status", UNSET)
        public_ipv4_status: PatchedPopRequestPublicIpv4Status | Unset
        if isinstance(_public_ipv4_status, Unset):
            public_ipv4_status = UNSET
        else:
            public_ipv4_status = check_patched_pop_request_public_ipv_4_status(_public_ipv4_status)

        _ipv6_status = d.pop("ipv6_status", UNSET)
        ipv6_status: PatchedPopRequestIpv6Status | Unset
        if isinstance(_ipv6_status, Unset):
            ipv6_status = UNSET
        else:
            ipv6_status = check_patched_pop_request_ipv_6_status(_ipv6_status)

        _bgp_status = d.pop("bgp_status", UNSET)
        bgp_status: PatchedPopRequestBgpStatus | Unset
        if isinstance(_bgp_status, Unset):
            bgp_status = UNSET
        else:
            bgp_status = check_patched_pop_request_bgp_status(_bgp_status)

        _byoip_status = d.pop("byoip_status", UNSET)
        byoip_status: PatchedPopRequestByoipStatus | Unset
        if isinstance(_byoip_status, Unset):
            byoip_status = UNSET
        else:
            byoip_status = check_patched_pop_request_byoip_status(_byoip_status)

        _own_rz = d.pop("own_rz", UNSET)
        own_rz: PatchedPopRequestOwnRz | Unset
        if isinstance(_own_rz, Unset):
            own_rz = UNSET
        else:
            own_rz = check_patched_pop_request_own_rz(_own_rz)

        _colocation = d.pop("colocation", UNSET)
        colocation: PatchedPopRequestColocation | Unset
        if isinstance(_colocation, Unset):
            colocation = UNSET
        else:
            colocation = check_patched_pop_request_colocation(_colocation)

        certification_evidence = d.pop("certification_evidence", UNSET)

        patched_pop_request = cls(
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
            provider_entity_id=provider_entity_id,
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

        patched_pop_request.additional_properties = d
        return patched_pop_request

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
