from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.provider_detail_request_api_public_docs import (
    ProviderDetailRequestApiPublicDocs,
    check_provider_detail_request_api_public_docs,
)
from ..models.provider_detail_request_billing_model import (
    ProviderDetailRequestBillingModel,
    check_provider_detail_request_billing_model,
)
from ..models.provider_detail_request_block_storage_status import (
    ProviderDetailRequestBlockStorageStatus,
    check_provider_detail_request_block_storage_status,
)
from ..models.provider_detail_request_bsi_grundschutz_status import (
    ProviderDetailRequestBsiGrundschutzStatus,
    check_provider_detail_request_bsi_grundschutz_status,
)
from ..models.provider_detail_request_c5_status import (
    ProviderDetailRequestC5Status,
    check_provider_detail_request_c5_status,
)
from ..models.provider_detail_request_cloud_init import (
    ProviderDetailRequestCloudInit,
    check_provider_detail_request_cloud_init,
)
from ..models.provider_detail_request_criticality_type_1 import (
    ProviderDetailRequestCriticalityType1,
    check_provider_detail_request_criticality_type_1,
)
from ..models.provider_detail_request_criticality_type_2_type_1 import (
    ProviderDetailRequestCriticalityType2Type1,
    check_provider_detail_request_criticality_type_2_type_1,
)
from ..models.provider_detail_request_criticality_type_3_type_1 import (
    ProviderDetailRequestCriticalityType3Type1,
    check_provider_detail_request_criticality_type_3_type_1,
)
from ..models.provider_detail_request_custom_images import (
    ProviderDetailRequestCustomImages,
    check_provider_detail_request_custom_images,
)
from ..models.provider_detail_request_dedicated_available import (
    ProviderDetailRequestDedicatedAvailable,
    check_provider_detail_request_dedicated_available,
)
from ..models.provider_detail_request_iso_27001_status import (
    ProviderDetailRequestIso27001Status,
    check_provider_detail_request_iso_27001_status,
)
from ..models.provider_detail_request_kind import ProviderDetailRequestKind, check_provider_detail_request_kind
from ..models.provider_detail_request_maintenance_api import (
    ProviderDetailRequestMaintenanceApi,
    check_provider_detail_request_maintenance_api,
)
from ..models.provider_detail_request_maintenance_scope import (
    ProviderDetailRequestMaintenanceScope,
    check_provider_detail_request_maintenance_scope,
)
from ..models.provider_detail_request_min_term import (
    ProviderDetailRequestMinTerm,
    check_provider_detail_request_min_term,
)
from ..models.provider_detail_request_provider import (
    ProviderDetailRequestProvider,
    check_provider_detail_request_provider,
)
from ..models.provider_detail_request_scoped_api_keys import (
    ProviderDetailRequestScopedApiKeys,
    check_provider_detail_request_scoped_api_keys,
)
from ..models.provider_detail_request_scs_iaas_status import (
    ProviderDetailRequestScsIaasStatus,
    check_provider_detail_request_scs_iaas_status,
)
from ..models.provider_detail_request_scs_kaas_status import (
    ProviderDetailRequestScsKaasStatus,
    check_provider_detail_request_scs_kaas_status,
)
from ..models.provider_detail_request_tenant_segmentation import (
    ProviderDetailRequestTenantSegmentation,
    check_provider_detail_request_tenant_segmentation,
)
from ..models.provider_detail_request_unified_api_across_locations import (
    ProviderDetailRequestUnifiedApiAcrossLocations,
    check_provider_detail_request_unified_api_across_locations,
)
from ..models.provider_detail_request_vm_available import (
    ProviderDetailRequestVmAvailable,
    check_provider_detail_request_vm_available,
)
from ..models.provider_detail_request_volume_discount import (
    ProviderDetailRequestVolumeDiscount,
    check_provider_detail_request_volume_discount,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderDetailRequest")


@_attrs_define
class ProviderDetailRequest:
    """Full detail serializer for Provider.

    Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
    resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
    Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

        Attributes:
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (ProviderDetailRequestProvider | Unset): * `loopback` - Loopback
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
            kind (ProviderDetailRequestKind | Unset): Type of provider (infrastructure, hardware, software)

                * `infrastructure` - Infrastructure
                * `hardware` - Hardware
                * `software` - Software
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (None | ProviderDetailRequestCriticalityType1 | ProviderDetailRequestCriticalityType2Type1 |
                ProviderDetailRequestCriticalityType3Type1 | Unset): Criticality level. Null = inherit from workspace, then org.
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
            legal_name (None | str | Unset): Legal company name (e.g. 'Hetzner Online GmbH')
            slug (None | str | Unset): URL-friendly identifier (auto-generated from name if empty)
            active (bool | Unset): When false, hidden from new PoP/DataSource/workspace PoP assignments.
            icon_content_type (None | str | Unset): MIME type of the icon (e.g., image/svg+xml, image/png)
            icon_filename (None | str | Unset): Original filename of the uploaded icon
            ccm_block (None | str | Unset): Polycrate block reference for the Cloud Controller Manager (e.g.
                cargo.ayedo.cloud/ayedo/k8s/hcloud-ccm)
            csi_controller_block (None | str | Unset): Polycrate block reference for the CSI driver (e.g.
                cargo.ayedo.cloud/ayedo/k8s/hcloud-csi)
            csi_storage_classes (Any | Unset): List of Kubernetes StorageClass names provided by this provider's CSI driver
                (e.g. ['hcloud-volumes'])
            address (None | str | Unset): Full postal address
            emails (Any | Unset): List of typed contact emails, e.g. [{"type": "billing", "email": "billing@example.com"}].
                Allowed types: billing, security, support, legal, notifications.
            phone (None | str | Unset): Phone number
            asn (Any | Unset): List of AS Numbers, e.g. [{"name": "Default", "value": "AS24940"}]
            urls (Any | Unset): List of named URLs, e.g. [{"name": "Support Portal", "url": "https://..."}]
            certifications (Any | Unset): List of certifications held by this provider (e.g. ISO27001, TISAX, SOC2)
            iso27001_status (ProviderDetailRequestIso27001Status | Unset): ISO 27001 status for this provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (ProviderDetailRequestC5Status | Unset): BSI C5 status for this provider.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            bsi_grundschutz_status (ProviderDetailRequestBsiGrundschutzStatus | Unset): BSI IT-Grundschutz status for this
                provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (ProviderDetailRequestScsIaasStatus | Unset): SCS-compatible IaaS status. Public chip only when
                compatible.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (ProviderDetailRequestScsKaasStatus | Unset): SCS-compatible KaaS status. Not the public SCS
                chip.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            unified_api_across_locations (ProviderDetailRequestUnifiedApiAcrossLocations | Unset): Whether the same API
                applies across this provider's locations.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            vm_available (ProviderDetailRequestVmAvailable | Unset): VM availability.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            dedicated_available (ProviderDetailRequestDedicatedAvailable | Unset): Dedicated server availability.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            cloud_init (ProviderDetailRequestCloudInit | Unset): cloud-init support.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            custom_images (ProviderDetailRequestCustomImages | Unset): Custom image support.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            api_public_docs (ProviderDetailRequestApiPublicDocs | Unset): Public API documentation is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            tenant_segmentation (ProviderDetailRequestTenantSegmentation | Unset): Tenant segmentation is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scoped_api_keys (ProviderDetailRequestScopedApiKeys | Unset): Scoped API keys are available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            maintenance_api (ProviderDetailRequestMaintenanceApi | Unset): Maintenance can be read via API.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            block_storage_status (ProviderDetailRequestBlockStorageStatus | Unset): Block storage is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            maintenance_scope (ProviderDetailRequestMaintenanceScope | Unset): Maintenance scope.

                * `system` - System
                * `object` - Object
                * `both` - Both
                * `unknown` - Unknown
            billing_model (ProviderDetailRequestBillingModel | Unset): Billing model. Not a price.

                * `monthly` - Monthly
                * `usage` - Usage
                * `both` - Both
            min_term (ProviderDetailRequestMinTerm | Unset): Minimum term. Not a price.

                * `none` - None
                * `3m` - 3 months
                * `6m` - 6 months
                * `12m` - 12 months
                * `custom` - Custom
            volume_discount (ProviderDetailRequestVolumeDiscount | Unset): Volume discount is offered. Not a price amount.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            uptime_sla (str | Unset): Short uptime SLA text. Not a price.
            certification_evidence (Any | Unset): HTTPS evidence URLs, e.g. [{"claim": "iso27001_status", "url":
                "https://..."}].
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderDetailRequestProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: ProviderDetailRequestKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: (
        None
        | ProviderDetailRequestCriticalityType1
        | ProviderDetailRequestCriticalityType2Type1
        | ProviderDetailRequestCriticalityType3Type1
        | Unset
    ) = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    icon_content_type: None | str | Unset = UNSET
    icon_filename: None | str | Unset = UNSET
    ccm_block: None | str | Unset = UNSET
    csi_controller_block: None | str | Unset = UNSET
    csi_storage_classes: Any | Unset = UNSET
    address: None | str | Unset = UNSET
    emails: Any | Unset = UNSET
    phone: None | str | Unset = UNSET
    asn: Any | Unset = UNSET
    urls: Any | Unset = UNSET
    certifications: Any | Unset = UNSET
    iso27001_status: ProviderDetailRequestIso27001Status | Unset = UNSET
    c5_status: ProviderDetailRequestC5Status | Unset = UNSET
    bsi_grundschutz_status: ProviderDetailRequestBsiGrundschutzStatus | Unset = UNSET
    scs_iaas_status: ProviderDetailRequestScsIaasStatus | Unset = UNSET
    scs_kaas_status: ProviderDetailRequestScsKaasStatus | Unset = UNSET
    unified_api_across_locations: ProviderDetailRequestUnifiedApiAcrossLocations | Unset = UNSET
    vm_available: ProviderDetailRequestVmAvailable | Unset = UNSET
    dedicated_available: ProviderDetailRequestDedicatedAvailable | Unset = UNSET
    cloud_init: ProviderDetailRequestCloudInit | Unset = UNSET
    custom_images: ProviderDetailRequestCustomImages | Unset = UNSET
    api_public_docs: ProviderDetailRequestApiPublicDocs | Unset = UNSET
    tenant_segmentation: ProviderDetailRequestTenantSegmentation | Unset = UNSET
    scoped_api_keys: ProviderDetailRequestScopedApiKeys | Unset = UNSET
    maintenance_api: ProviderDetailRequestMaintenanceApi | Unset = UNSET
    block_storage_status: ProviderDetailRequestBlockStorageStatus | Unset = UNSET
    maintenance_scope: ProviderDetailRequestMaintenanceScope | Unset = UNSET
    billing_model: ProviderDetailRequestBillingModel | Unset = UNSET
    min_term: ProviderDetailRequestMinTerm | Unset = UNSET
    volume_discount: ProviderDetailRequestVolumeDiscount | Unset = UNSET
    uptime_sla: str | Unset = UNSET
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

        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        active = self.active

        icon_content_type: None | str | Unset
        if isinstance(self.icon_content_type, Unset):
            icon_content_type = UNSET
        else:
            icon_content_type = self.icon_content_type

        icon_filename: None | str | Unset
        if isinstance(self.icon_filename, Unset):
            icon_filename = UNSET
        else:
            icon_filename = self.icon_filename

        ccm_block: None | str | Unset
        if isinstance(self.ccm_block, Unset):
            ccm_block = UNSET
        else:
            ccm_block = self.ccm_block

        csi_controller_block: None | str | Unset
        if isinstance(self.csi_controller_block, Unset):
            csi_controller_block = UNSET
        else:
            csi_controller_block = self.csi_controller_block

        csi_storage_classes = self.csi_storage_classes

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        emails = self.emails

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        asn = self.asn

        urls = self.urls

        certifications = self.certifications

        iso27001_status: str | Unset = UNSET
        if not isinstance(self.iso27001_status, Unset):
            iso27001_status = self.iso27001_status

        c5_status: str | Unset = UNSET
        if not isinstance(self.c5_status, Unset):
            c5_status = self.c5_status

        bsi_grundschutz_status: str | Unset = UNSET
        if not isinstance(self.bsi_grundschutz_status, Unset):
            bsi_grundschutz_status = self.bsi_grundschutz_status

        scs_iaas_status: str | Unset = UNSET
        if not isinstance(self.scs_iaas_status, Unset):
            scs_iaas_status = self.scs_iaas_status

        scs_kaas_status: str | Unset = UNSET
        if not isinstance(self.scs_kaas_status, Unset):
            scs_kaas_status = self.scs_kaas_status

        unified_api_across_locations: str | Unset = UNSET
        if not isinstance(self.unified_api_across_locations, Unset):
            unified_api_across_locations = self.unified_api_across_locations

        vm_available: str | Unset = UNSET
        if not isinstance(self.vm_available, Unset):
            vm_available = self.vm_available

        dedicated_available: str | Unset = UNSET
        if not isinstance(self.dedicated_available, Unset):
            dedicated_available = self.dedicated_available

        cloud_init: str | Unset = UNSET
        if not isinstance(self.cloud_init, Unset):
            cloud_init = self.cloud_init

        custom_images: str | Unset = UNSET
        if not isinstance(self.custom_images, Unset):
            custom_images = self.custom_images

        api_public_docs: str | Unset = UNSET
        if not isinstance(self.api_public_docs, Unset):
            api_public_docs = self.api_public_docs

        tenant_segmentation: str | Unset = UNSET
        if not isinstance(self.tenant_segmentation, Unset):
            tenant_segmentation = self.tenant_segmentation

        scoped_api_keys: str | Unset = UNSET
        if not isinstance(self.scoped_api_keys, Unset):
            scoped_api_keys = self.scoped_api_keys

        maintenance_api: str | Unset = UNSET
        if not isinstance(self.maintenance_api, Unset):
            maintenance_api = self.maintenance_api

        block_storage_status: str | Unset = UNSET
        if not isinstance(self.block_storage_status, Unset):
            block_storage_status = self.block_storage_status

        maintenance_scope: str | Unset = UNSET
        if not isinstance(self.maintenance_scope, Unset):
            maintenance_scope = self.maintenance_scope

        billing_model: str | Unset = UNSET
        if not isinstance(self.billing_model, Unset):
            billing_model = self.billing_model

        min_term: str | Unset = UNSET
        if not isinstance(self.min_term, Unset):
            min_term = self.min_term

        volume_discount: str | Unset = UNSET
        if not isinstance(self.volume_discount, Unset):
            volume_discount = self.volume_discount

        uptime_sla = self.uptime_sla

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
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if active is not UNSET:
            field_dict["active"] = active
        if icon_content_type is not UNSET:
            field_dict["icon_content_type"] = icon_content_type
        if icon_filename is not UNSET:
            field_dict["icon_filename"] = icon_filename
        if ccm_block is not UNSET:
            field_dict["ccm_block"] = ccm_block
        if csi_controller_block is not UNSET:
            field_dict["csi_controller_block"] = csi_controller_block
        if csi_storage_classes is not UNSET:
            field_dict["csi_storage_classes"] = csi_storage_classes
        if address is not UNSET:
            field_dict["address"] = address
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phone is not UNSET:
            field_dict["phone"] = phone
        if asn is not UNSET:
            field_dict["asn"] = asn
        if urls is not UNSET:
            field_dict["urls"] = urls
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if iso27001_status is not UNSET:
            field_dict["iso27001_status"] = iso27001_status
        if c5_status is not UNSET:
            field_dict["c5_status"] = c5_status
        if bsi_grundschutz_status is not UNSET:
            field_dict["bsi_grundschutz_status"] = bsi_grundschutz_status
        if scs_iaas_status is not UNSET:
            field_dict["scs_iaas_status"] = scs_iaas_status
        if scs_kaas_status is not UNSET:
            field_dict["scs_kaas_status"] = scs_kaas_status
        if unified_api_across_locations is not UNSET:
            field_dict["unified_api_across_locations"] = unified_api_across_locations
        if vm_available is not UNSET:
            field_dict["vm_available"] = vm_available
        if dedicated_available is not UNSET:
            field_dict["dedicated_available"] = dedicated_available
        if cloud_init is not UNSET:
            field_dict["cloud_init"] = cloud_init
        if custom_images is not UNSET:
            field_dict["custom_images"] = custom_images
        if api_public_docs is not UNSET:
            field_dict["api_public_docs"] = api_public_docs
        if tenant_segmentation is not UNSET:
            field_dict["tenant_segmentation"] = tenant_segmentation
        if scoped_api_keys is not UNSET:
            field_dict["scoped_api_keys"] = scoped_api_keys
        if maintenance_api is not UNSET:
            field_dict["maintenance_api"] = maintenance_api
        if block_storage_status is not UNSET:
            field_dict["block_storage_status"] = block_storage_status
        if maintenance_scope is not UNSET:
            field_dict["maintenance_scope"] = maintenance_scope
        if billing_model is not UNSET:
            field_dict["billing_model"] = billing_model
        if min_term is not UNSET:
            field_dict["min_term"] = min_term
        if volume_discount is not UNSET:
            field_dict["volume_discount"] = volume_discount
        if uptime_sla is not UNSET:
            field_dict["uptime_sla"] = uptime_sla
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

        if not isinstance(self.legal_name, Unset):
            if isinstance(self.legal_name, str):
                files.append(("legal_name", (None, str(self.legal_name).encode(), "text/plain")))
            else:
                files.append(("legal_name", (None, str(self.legal_name).encode(), "text/plain")))

        if not isinstance(self.slug, Unset):
            if isinstance(self.slug, str):
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))
            else:
                files.append(("slug", (None, str(self.slug).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.icon_content_type, Unset):
            if isinstance(self.icon_content_type, str):
                files.append(("icon_content_type", (None, str(self.icon_content_type).encode(), "text/plain")))
            else:
                files.append(("icon_content_type", (None, str(self.icon_content_type).encode(), "text/plain")))

        if not isinstance(self.icon_filename, Unset):
            if isinstance(self.icon_filename, str):
                files.append(("icon_filename", (None, str(self.icon_filename).encode(), "text/plain")))
            else:
                files.append(("icon_filename", (None, str(self.icon_filename).encode(), "text/plain")))

        if not isinstance(self.ccm_block, Unset):
            if isinstance(self.ccm_block, str):
                files.append(("ccm_block", (None, str(self.ccm_block).encode(), "text/plain")))
            else:
                files.append(("ccm_block", (None, str(self.ccm_block).encode(), "text/plain")))

        if not isinstance(self.csi_controller_block, Unset):
            if isinstance(self.csi_controller_block, str):
                files.append(("csi_controller_block", (None, str(self.csi_controller_block).encode(), "text/plain")))
            else:
                files.append(("csi_controller_block", (None, str(self.csi_controller_block).encode(), "text/plain")))

        if not isinstance(self.csi_storage_classes, Unset):
            files.append(("csi_storage_classes", (None, str(self.csi_storage_classes).encode(), "text/plain")))

        if not isinstance(self.address, Unset):
            if isinstance(self.address, str):
                files.append(("address", (None, str(self.address).encode(), "text/plain")))
            else:
                files.append(("address", (None, str(self.address).encode(), "text/plain")))

        if not isinstance(self.emails, Unset):
            files.append(("emails", (None, str(self.emails).encode(), "text/plain")))

        if not isinstance(self.phone, Unset):
            if isinstance(self.phone, str):
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))
            else:
                files.append(("phone", (None, str(self.phone).encode(), "text/plain")))

        if not isinstance(self.asn, Unset):
            files.append(("asn", (None, str(self.asn).encode(), "text/plain")))

        if not isinstance(self.urls, Unset):
            files.append(("urls", (None, str(self.urls).encode(), "text/plain")))

        if not isinstance(self.certifications, Unset):
            files.append(("certifications", (None, str(self.certifications).encode(), "text/plain")))

        if not isinstance(self.iso27001_status, Unset):
            files.append(("iso27001_status", (None, str(self.iso27001_status).encode(), "text/plain")))

        if not isinstance(self.c5_status, Unset):
            files.append(("c5_status", (None, str(self.c5_status).encode(), "text/plain")))

        if not isinstance(self.bsi_grundschutz_status, Unset):
            files.append(("bsi_grundschutz_status", (None, str(self.bsi_grundschutz_status).encode(), "text/plain")))

        if not isinstance(self.scs_iaas_status, Unset):
            files.append(("scs_iaas_status", (None, str(self.scs_iaas_status).encode(), "text/plain")))

        if not isinstance(self.scs_kaas_status, Unset):
            files.append(("scs_kaas_status", (None, str(self.scs_kaas_status).encode(), "text/plain")))

        if not isinstance(self.unified_api_across_locations, Unset):
            files.append(
                ("unified_api_across_locations", (None, str(self.unified_api_across_locations).encode(), "text/plain"))
            )

        if not isinstance(self.vm_available, Unset):
            files.append(("vm_available", (None, str(self.vm_available).encode(), "text/plain")))

        if not isinstance(self.dedicated_available, Unset):
            files.append(("dedicated_available", (None, str(self.dedicated_available).encode(), "text/plain")))

        if not isinstance(self.cloud_init, Unset):
            files.append(("cloud_init", (None, str(self.cloud_init).encode(), "text/plain")))

        if not isinstance(self.custom_images, Unset):
            files.append(("custom_images", (None, str(self.custom_images).encode(), "text/plain")))

        if not isinstance(self.api_public_docs, Unset):
            files.append(("api_public_docs", (None, str(self.api_public_docs).encode(), "text/plain")))

        if not isinstance(self.tenant_segmentation, Unset):
            files.append(("tenant_segmentation", (None, str(self.tenant_segmentation).encode(), "text/plain")))

        if not isinstance(self.scoped_api_keys, Unset):
            files.append(("scoped_api_keys", (None, str(self.scoped_api_keys).encode(), "text/plain")))

        if not isinstance(self.maintenance_api, Unset):
            files.append(("maintenance_api", (None, str(self.maintenance_api).encode(), "text/plain")))

        if not isinstance(self.block_storage_status, Unset):
            files.append(("block_storage_status", (None, str(self.block_storage_status).encode(), "text/plain")))

        if not isinstance(self.maintenance_scope, Unset):
            files.append(("maintenance_scope", (None, str(self.maintenance_scope).encode(), "text/plain")))

        if not isinstance(self.billing_model, Unset):
            files.append(("billing_model", (None, str(self.billing_model).encode(), "text/plain")))

        if not isinstance(self.min_term, Unset):
            files.append(("min_term", (None, str(self.min_term).encode(), "text/plain")))

        if not isinstance(self.volume_discount, Unset):
            files.append(("volume_discount", (None, str(self.volume_discount).encode(), "text/plain")))

        if not isinstance(self.uptime_sla, Unset):
            files.append(("uptime_sla", (None, str(self.uptime_sla).encode(), "text/plain")))

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
        provider: ProviderDetailRequestProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_detail_request_provider(_provider)

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
        kind: ProviderDetailRequestKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_provider_detail_request_kind(_kind)

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
            | ProviderDetailRequestCriticalityType1
            | ProviderDetailRequestCriticalityType2Type1
            | ProviderDetailRequestCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_provider_detail_request_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_provider_detail_request_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_provider_detail_request_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ProviderDetailRequestCriticalityType1
                | ProviderDetailRequestCriticalityType2Type1
                | ProviderDetailRequestCriticalityType3Type1
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

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        active = d.pop("active", UNSET)

        def _parse_icon_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_content_type = _parse_icon_content_type(d.pop("icon_content_type", UNSET))

        def _parse_icon_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_filename = _parse_icon_filename(d.pop("icon_filename", UNSET))

        def _parse_ccm_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ccm_block = _parse_ccm_block(d.pop("ccm_block", UNSET))

        def _parse_csi_controller_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csi_controller_block = _parse_csi_controller_block(d.pop("csi_controller_block", UNSET))

        csi_storage_classes = d.pop("csi_storage_classes", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        emails = d.pop("emails", UNSET)

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        asn = d.pop("asn", UNSET)

        urls = d.pop("urls", UNSET)

        certifications = d.pop("certifications", UNSET)

        _iso27001_status = d.pop("iso27001_status", UNSET)
        iso27001_status: ProviderDetailRequestIso27001Status | Unset
        if isinstance(_iso27001_status, Unset):
            iso27001_status = UNSET
        else:
            iso27001_status = check_provider_detail_request_iso_27001_status(_iso27001_status)

        _c5_status = d.pop("c5_status", UNSET)
        c5_status: ProviderDetailRequestC5Status | Unset
        if isinstance(_c5_status, Unset):
            c5_status = UNSET
        else:
            c5_status = check_provider_detail_request_c5_status(_c5_status)

        _bsi_grundschutz_status = d.pop("bsi_grundschutz_status", UNSET)
        bsi_grundschutz_status: ProviderDetailRequestBsiGrundschutzStatus | Unset
        if isinstance(_bsi_grundschutz_status, Unset):
            bsi_grundschutz_status = UNSET
        else:
            bsi_grundschutz_status = check_provider_detail_request_bsi_grundschutz_status(_bsi_grundschutz_status)

        _scs_iaas_status = d.pop("scs_iaas_status", UNSET)
        scs_iaas_status: ProviderDetailRequestScsIaasStatus | Unset
        if isinstance(_scs_iaas_status, Unset):
            scs_iaas_status = UNSET
        else:
            scs_iaas_status = check_provider_detail_request_scs_iaas_status(_scs_iaas_status)

        _scs_kaas_status = d.pop("scs_kaas_status", UNSET)
        scs_kaas_status: ProviderDetailRequestScsKaasStatus | Unset
        if isinstance(_scs_kaas_status, Unset):
            scs_kaas_status = UNSET
        else:
            scs_kaas_status = check_provider_detail_request_scs_kaas_status(_scs_kaas_status)

        _unified_api_across_locations = d.pop("unified_api_across_locations", UNSET)
        unified_api_across_locations: ProviderDetailRequestUnifiedApiAcrossLocations | Unset
        if isinstance(_unified_api_across_locations, Unset):
            unified_api_across_locations = UNSET
        else:
            unified_api_across_locations = check_provider_detail_request_unified_api_across_locations(
                _unified_api_across_locations
            )

        _vm_available = d.pop("vm_available", UNSET)
        vm_available: ProviderDetailRequestVmAvailable | Unset
        if isinstance(_vm_available, Unset):
            vm_available = UNSET
        else:
            vm_available = check_provider_detail_request_vm_available(_vm_available)

        _dedicated_available = d.pop("dedicated_available", UNSET)
        dedicated_available: ProviderDetailRequestDedicatedAvailable | Unset
        if isinstance(_dedicated_available, Unset):
            dedicated_available = UNSET
        else:
            dedicated_available = check_provider_detail_request_dedicated_available(_dedicated_available)

        _cloud_init = d.pop("cloud_init", UNSET)
        cloud_init: ProviderDetailRequestCloudInit | Unset
        if isinstance(_cloud_init, Unset):
            cloud_init = UNSET
        else:
            cloud_init = check_provider_detail_request_cloud_init(_cloud_init)

        _custom_images = d.pop("custom_images", UNSET)
        custom_images: ProviderDetailRequestCustomImages | Unset
        if isinstance(_custom_images, Unset):
            custom_images = UNSET
        else:
            custom_images = check_provider_detail_request_custom_images(_custom_images)

        _api_public_docs = d.pop("api_public_docs", UNSET)
        api_public_docs: ProviderDetailRequestApiPublicDocs | Unset
        if isinstance(_api_public_docs, Unset):
            api_public_docs = UNSET
        else:
            api_public_docs = check_provider_detail_request_api_public_docs(_api_public_docs)

        _tenant_segmentation = d.pop("tenant_segmentation", UNSET)
        tenant_segmentation: ProviderDetailRequestTenantSegmentation | Unset
        if isinstance(_tenant_segmentation, Unset):
            tenant_segmentation = UNSET
        else:
            tenant_segmentation = check_provider_detail_request_tenant_segmentation(_tenant_segmentation)

        _scoped_api_keys = d.pop("scoped_api_keys", UNSET)
        scoped_api_keys: ProviderDetailRequestScopedApiKeys | Unset
        if isinstance(_scoped_api_keys, Unset):
            scoped_api_keys = UNSET
        else:
            scoped_api_keys = check_provider_detail_request_scoped_api_keys(_scoped_api_keys)

        _maintenance_api = d.pop("maintenance_api", UNSET)
        maintenance_api: ProviderDetailRequestMaintenanceApi | Unset
        if isinstance(_maintenance_api, Unset):
            maintenance_api = UNSET
        else:
            maintenance_api = check_provider_detail_request_maintenance_api(_maintenance_api)

        _block_storage_status = d.pop("block_storage_status", UNSET)
        block_storage_status: ProviderDetailRequestBlockStorageStatus | Unset
        if isinstance(_block_storage_status, Unset):
            block_storage_status = UNSET
        else:
            block_storage_status = check_provider_detail_request_block_storage_status(_block_storage_status)

        _maintenance_scope = d.pop("maintenance_scope", UNSET)
        maintenance_scope: ProviderDetailRequestMaintenanceScope | Unset
        if isinstance(_maintenance_scope, Unset):
            maintenance_scope = UNSET
        else:
            maintenance_scope = check_provider_detail_request_maintenance_scope(_maintenance_scope)

        _billing_model = d.pop("billing_model", UNSET)
        billing_model: ProviderDetailRequestBillingModel | Unset
        if isinstance(_billing_model, Unset):
            billing_model = UNSET
        else:
            billing_model = check_provider_detail_request_billing_model(_billing_model)

        _min_term = d.pop("min_term", UNSET)
        min_term: ProviderDetailRequestMinTerm | Unset
        if isinstance(_min_term, Unset):
            min_term = UNSET
        else:
            min_term = check_provider_detail_request_min_term(_min_term)

        _volume_discount = d.pop("volume_discount", UNSET)
        volume_discount: ProviderDetailRequestVolumeDiscount | Unset
        if isinstance(_volume_discount, Unset):
            volume_discount = UNSET
        else:
            volume_discount = check_provider_detail_request_volume_discount(_volume_discount)

        uptime_sla = d.pop("uptime_sla", UNSET)

        certification_evidence = d.pop("certification_evidence", UNSET)

        provider_detail_request = cls(
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
            legal_name=legal_name,
            slug=slug,
            active=active,
            icon_content_type=icon_content_type,
            icon_filename=icon_filename,
            ccm_block=ccm_block,
            csi_controller_block=csi_controller_block,
            csi_storage_classes=csi_storage_classes,
            address=address,
            emails=emails,
            phone=phone,
            asn=asn,
            urls=urls,
            certifications=certifications,
            iso27001_status=iso27001_status,
            c5_status=c5_status,
            bsi_grundschutz_status=bsi_grundschutz_status,
            scs_iaas_status=scs_iaas_status,
            scs_kaas_status=scs_kaas_status,
            unified_api_across_locations=unified_api_across_locations,
            vm_available=vm_available,
            dedicated_available=dedicated_available,
            cloud_init=cloud_init,
            custom_images=custom_images,
            api_public_docs=api_public_docs,
            tenant_segmentation=tenant_segmentation,
            scoped_api_keys=scoped_api_keys,
            maintenance_api=maintenance_api,
            block_storage_status=block_storage_status,
            maintenance_scope=maintenance_scope,
            billing_model=billing_model,
            min_term=min_term,
            volume_discount=volume_discount,
            uptime_sla=uptime_sla,
            certification_evidence=certification_evidence,
        )

        provider_detail_request.additional_properties = d
        return provider_detail_request

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
