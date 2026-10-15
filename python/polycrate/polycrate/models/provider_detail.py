from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_detail_api_public_docs import ProviderDetailApiPublicDocs, check_provider_detail_api_public_docs
from ..models.provider_detail_billing_model import ProviderDetailBillingModel, check_provider_detail_billing_model
from ..models.provider_detail_block_storage_status import (
    ProviderDetailBlockStorageStatus,
    check_provider_detail_block_storage_status,
)
from ..models.provider_detail_bsi_grundschutz_status import (
    ProviderDetailBsiGrundschutzStatus,
    check_provider_detail_bsi_grundschutz_status,
)
from ..models.provider_detail_c5_status import ProviderDetailC5Status, check_provider_detail_c5_status
from ..models.provider_detail_cloud_init import ProviderDetailCloudInit, check_provider_detail_cloud_init
from ..models.provider_detail_criticality_type_1 import (
    ProviderDetailCriticalityType1,
    check_provider_detail_criticality_type_1,
)
from ..models.provider_detail_criticality_type_2_type_1 import (
    ProviderDetailCriticalityType2Type1,
    check_provider_detail_criticality_type_2_type_1,
)
from ..models.provider_detail_criticality_type_3_type_1 import (
    ProviderDetailCriticalityType3Type1,
    check_provider_detail_criticality_type_3_type_1,
)
from ..models.provider_detail_custom_images import ProviderDetailCustomImages, check_provider_detail_custom_images
from ..models.provider_detail_dedicated_available import (
    ProviderDetailDedicatedAvailable,
    check_provider_detail_dedicated_available,
)
from ..models.provider_detail_effective_criticality_type_1 import (
    ProviderDetailEffectiveCriticalityType1,
    check_provider_detail_effective_criticality_type_1,
)
from ..models.provider_detail_effective_criticality_type_2_type_1 import (
    ProviderDetailEffectiveCriticalityType2Type1,
    check_provider_detail_effective_criticality_type_2_type_1,
)
from ..models.provider_detail_effective_criticality_type_3_type_1 import (
    ProviderDetailEffectiveCriticalityType3Type1,
    check_provider_detail_effective_criticality_type_3_type_1,
)
from ..models.provider_detail_iso_27001_status import (
    ProviderDetailIso27001Status,
    check_provider_detail_iso_27001_status,
)
from ..models.provider_detail_kind import ProviderDetailKind, check_provider_detail_kind
from ..models.provider_detail_last_state import ProviderDetailLastState, check_provider_detail_last_state
from ..models.provider_detail_maintenance_api import ProviderDetailMaintenanceApi, check_provider_detail_maintenance_api
from ..models.provider_detail_maintenance_scope import (
    ProviderDetailMaintenanceScope,
    check_provider_detail_maintenance_scope,
)
from ..models.provider_detail_min_term import ProviderDetailMinTerm, check_provider_detail_min_term
from ..models.provider_detail_provider import ProviderDetailProvider, check_provider_detail_provider
from ..models.provider_detail_scope import ProviderDetailScope, check_provider_detail_scope
from ..models.provider_detail_scoped_api_keys import ProviderDetailScopedApiKeys, check_provider_detail_scoped_api_keys
from ..models.provider_detail_scs_iaas_status import ProviderDetailScsIaasStatus, check_provider_detail_scs_iaas_status
from ..models.provider_detail_scs_kaas_status import ProviderDetailScsKaasStatus, check_provider_detail_scs_kaas_status
from ..models.provider_detail_state import ProviderDetailState, check_provider_detail_state
from ..models.provider_detail_tenant_segmentation import (
    ProviderDetailTenantSegmentation,
    check_provider_detail_tenant_segmentation,
)
from ..models.provider_detail_unified_api_across_locations import (
    ProviderDetailUnifiedApiAcrossLocations,
    check_provider_detail_unified_api_across_locations,
)
from ..models.provider_detail_vm_available import ProviderDetailVmAvailable, check_provider_detail_vm_available
from ..models.provider_detail_volume_discount import ProviderDetailVolumeDiscount, check_provider_detail_volume_discount
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_detail_created import ProviderDetailCreated
    from ..models.provider_detail_deleted_by_user_type_0 import ProviderDetailDeletedByUserType0
    from ..models.provider_detail_last_action_run_type_0 import ProviderDetailLastActionRunType0
    from ..models.provider_detail_organization_type_0 import ProviderDetailOrganizationType0
    from ..models.provider_detail_workspace_type_0 import ProviderDetailWorkspaceType0


T = TypeVar("T", bound="ProviderDetail")


@_attrs_define
class ProviderDetail:
    """Full detail serializer for Provider.

    Inherits icon_url + is_class_icon from ManagedObjectDetailSerializer (both use
    resolve_managed_object_icon_url which falls back to class_icon_url). has_icon is
    Provider-specific and added here. icon_data (BinaryField) is excluded intentionally.

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (None | ProviderDetailDeletedByUserType0):
            state (ProviderDetailState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (ProviderDetailLastState): * `OK` - Ok
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
            scope (ProviderDetailScope): The scope is used to separate `system` owned objects from `user` owned objects.

                * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            effective_criticality (None | ProviderDetailEffectiveCriticalityType1 |
                ProviderDetailEffectiveCriticalityType2Type1 | ProviderDetailEffectiveCriticalityType3Type1):
            actual_availability (str): Calculated actual availability as yearly average in %
            organization (None | ProviderDetailOrganizationType0):
            workspace (None | ProviderDetailWorkspaceType0):
            created (ProviderDetailCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (None | ProviderDetailLastActionRunType0):
            has_icon (bool):
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (ProviderDetailProvider | Unset): * `loopback` - Loopback
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
            kind (ProviderDetailKind | Unset): Type of provider (infrastructure, hardware, software)

                * `infrastructure` - Infrastructure
                * `hardware` - Hardware
                * `software` - Software
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (None | ProviderDetailCriticalityType1 | ProviderDetailCriticalityType2Type1 |
                ProviderDetailCriticalityType3Type1 | Unset): Criticality level. Null = inherit from workspace, then org.
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
            iso27001_status (ProviderDetailIso27001Status | Unset): ISO 27001 status for this provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            c5_status (ProviderDetailC5Status | Unset): BSI C5 status for this provider.

                * `none` - None
                * `planned` - Planned
                * `typ1` - Type 1
                * `typ2` - Type 2
            bsi_grundschutz_status (ProviderDetailBsiGrundschutzStatus | Unset): BSI IT-Grundschutz status for this
                provider.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scs_iaas_status (ProviderDetailScsIaasStatus | Unset): SCS-compatible IaaS status. Public chip only when
                compatible.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            scs_kaas_status (ProviderDetailScsKaasStatus | Unset): SCS-compatible KaaS status. Not the public SCS chip.

                * `none` - None
                * `compatible` - Compatible
                * `listed_not_certified` - Listed, not certified
            unified_api_across_locations (ProviderDetailUnifiedApiAcrossLocations | Unset): Whether the same API applies
                across this provider's locations.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            vm_available (ProviderDetailVmAvailable | Unset): VM availability.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            dedicated_available (ProviderDetailDedicatedAvailable | Unset): Dedicated server availability.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            cloud_init (ProviderDetailCloudInit | Unset): cloud-init support.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            custom_images (ProviderDetailCustomImages | Unset): Custom image support.

                * `yes` - Yes
                * `no` - No
                * `planned` - Planned
            api_public_docs (ProviderDetailApiPublicDocs | Unset): Public API documentation is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            tenant_segmentation (ProviderDetailTenantSegmentation | Unset): Tenant segmentation is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            scoped_api_keys (ProviderDetailScopedApiKeys | Unset): Scoped API keys are available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            maintenance_api (ProviderDetailMaintenanceApi | Unset): Maintenance can be read via API.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            block_storage_status (ProviderDetailBlockStorageStatus | Unset): Block storage is available.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            maintenance_scope (ProviderDetailMaintenanceScope | Unset): Maintenance scope.

                * `system` - System
                * `object` - Object
                * `both` - Both
                * `unknown` - Unknown
            billing_model (ProviderDetailBillingModel | Unset): Billing model. Not a price.

                * `monthly` - Monthly
                * `usage` - Usage
                * `both` - Both
            min_term (ProviderDetailMinTerm | Unset): Minimum term. Not a price.

                * `none` - None
                * `3m` - 3 months
                * `6m` - 6 months
                * `12m` - 12 months
                * `custom` - Custom
            volume_discount (ProviderDetailVolumeDiscount | Unset): Volume discount is offered. Not a price amount.

                * `unknown` - Unknown
                * `no` - No
                * `planned` - Planned
                * `yes` - Yes
            uptime_sla (str | Unset): Short uptime SLA text. Not a price.
            certification_evidence (Any | Unset): HTTPS evidence URLs, e.g. [{"claim": "iso27001_status", "url":
                "https://..."}].
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: None | ProviderDetailDeletedByUserType0
    state: ProviderDetailState
    state_reason: None | str
    last_state: ProviderDetailLastState
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
    scope: ProviderDetailScope
    conditions: Any
    effective_criticality: (
        None
        | ProviderDetailEffectiveCriticalityType1
        | ProviderDetailEffectiveCriticalityType2Type1
        | ProviderDetailEffectiveCriticalityType3Type1
    )
    actual_availability: str
    organization: None | ProviderDetailOrganizationType0
    workspace: None | ProviderDetailWorkspaceType0
    created: ProviderDetailCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: None | ProviderDetailLastActionRunType0
    has_icon: bool
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderDetailProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: ProviderDetailKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: (
        None
        | ProviderDetailCriticalityType1
        | ProviderDetailCriticalityType2Type1
        | ProviderDetailCriticalityType3Type1
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
    iso27001_status: ProviderDetailIso27001Status | Unset = UNSET
    c5_status: ProviderDetailC5Status | Unset = UNSET
    bsi_grundschutz_status: ProviderDetailBsiGrundschutzStatus | Unset = UNSET
    scs_iaas_status: ProviderDetailScsIaasStatus | Unset = UNSET
    scs_kaas_status: ProviderDetailScsKaasStatus | Unset = UNSET
    unified_api_across_locations: ProviderDetailUnifiedApiAcrossLocations | Unset = UNSET
    vm_available: ProviderDetailVmAvailable | Unset = UNSET
    dedicated_available: ProviderDetailDedicatedAvailable | Unset = UNSET
    cloud_init: ProviderDetailCloudInit | Unset = UNSET
    custom_images: ProviderDetailCustomImages | Unset = UNSET
    api_public_docs: ProviderDetailApiPublicDocs | Unset = UNSET
    tenant_segmentation: ProviderDetailTenantSegmentation | Unset = UNSET
    scoped_api_keys: ProviderDetailScopedApiKeys | Unset = UNSET
    maintenance_api: ProviderDetailMaintenanceApi | Unset = UNSET
    block_storage_status: ProviderDetailBlockStorageStatus | Unset = UNSET
    maintenance_scope: ProviderDetailMaintenanceScope | Unset = UNSET
    billing_model: ProviderDetailBillingModel | Unset = UNSET
    min_term: ProviderDetailMinTerm | Unset = UNSET
    volume_discount: ProviderDetailVolumeDiscount | Unset = UNSET
    uptime_sla: str | Unset = UNSET
    certification_evidence: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_detail_deleted_by_user_type_0 import ProviderDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.provider_detail_last_action_run_type_0 import ProviderDetailLastActionRunType0  # noqa: PLC0415
        from ..models.provider_detail_organization_type_0 import ProviderDetailOrganizationType0  # noqa: PLC0415
        from ..models.provider_detail_workspace_type_0 import ProviderDetailWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, ProviderDetailDeletedByUserType0):
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
        if isinstance(self.organization, ProviderDetailOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ProviderDetailWorkspaceType0):
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
        if isinstance(self.last_action_run, ProviderDetailLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        has_icon = self.has_icon

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
                "has_icon": has_icon,
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_detail_created import ProviderDetailCreated  # noqa: PLC0415
        from ..models.provider_detail_deleted_by_user_type_0 import ProviderDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.provider_detail_last_action_run_type_0 import ProviderDetailLastActionRunType0  # noqa: PLC0415
        from ..models.provider_detail_organization_type_0 import ProviderDetailOrganizationType0  # noqa: PLC0415
        from ..models.provider_detail_workspace_type_0 import ProviderDetailWorkspaceType0  # noqa: PLC0415

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

        def _parse_deleted_by_user(data: object) -> None | ProviderDetailDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = ProviderDetailDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderDetailDeletedByUserType0, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        state = check_provider_detail_state(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_provider_detail_last_state(d.pop("last_state"))

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

        scope = check_provider_detail_scope(d.pop("scope"))

        conditions = d.pop("conditions")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            None
            | ProviderDetailEffectiveCriticalityType1
            | ProviderDetailEffectiveCriticalityType2Type1
            | ProviderDetailEffectiveCriticalityType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_provider_detail_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_provider_detail_effective_criticality_type_2_type_1(data)

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_provider_detail_effective_criticality_type_3_type_1(data)

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ProviderDetailEffectiveCriticalityType1
                | ProviderDetailEffectiveCriticalityType2Type1
                | ProviderDetailEffectiveCriticalityType3Type1,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        actual_availability = d.pop("actual_availability")

        def _parse_organization(data: object) -> None | ProviderDetailOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ProviderDetailOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderDetailOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> None | ProviderDetailWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ProviderDetailWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderDetailWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ProviderDetailCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> None | ProviderDetailLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = ProviderDetailLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderDetailLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        has_icon = d.pop("has_icon")

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
        provider: ProviderDetailProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_detail_provider(_provider)

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
        kind: ProviderDetailKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_provider_detail_kind(_kind)

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
            | ProviderDetailCriticalityType1
            | ProviderDetailCriticalityType2Type1
            | ProviderDetailCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_provider_detail_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_provider_detail_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_provider_detail_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ProviderDetailCriticalityType1
                | ProviderDetailCriticalityType2Type1
                | ProviderDetailCriticalityType3Type1
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
        iso27001_status: ProviderDetailIso27001Status | Unset
        if isinstance(_iso27001_status, Unset):
            iso27001_status = UNSET
        else:
            iso27001_status = check_provider_detail_iso_27001_status(_iso27001_status)

        _c5_status = d.pop("c5_status", UNSET)
        c5_status: ProviderDetailC5Status | Unset
        if isinstance(_c5_status, Unset):
            c5_status = UNSET
        else:
            c5_status = check_provider_detail_c5_status(_c5_status)

        _bsi_grundschutz_status = d.pop("bsi_grundschutz_status", UNSET)
        bsi_grundschutz_status: ProviderDetailBsiGrundschutzStatus | Unset
        if isinstance(_bsi_grundschutz_status, Unset):
            bsi_grundschutz_status = UNSET
        else:
            bsi_grundschutz_status = check_provider_detail_bsi_grundschutz_status(_bsi_grundschutz_status)

        _scs_iaas_status = d.pop("scs_iaas_status", UNSET)
        scs_iaas_status: ProviderDetailScsIaasStatus | Unset
        if isinstance(_scs_iaas_status, Unset):
            scs_iaas_status = UNSET
        else:
            scs_iaas_status = check_provider_detail_scs_iaas_status(_scs_iaas_status)

        _scs_kaas_status = d.pop("scs_kaas_status", UNSET)
        scs_kaas_status: ProviderDetailScsKaasStatus | Unset
        if isinstance(_scs_kaas_status, Unset):
            scs_kaas_status = UNSET
        else:
            scs_kaas_status = check_provider_detail_scs_kaas_status(_scs_kaas_status)

        _unified_api_across_locations = d.pop("unified_api_across_locations", UNSET)
        unified_api_across_locations: ProviderDetailUnifiedApiAcrossLocations | Unset
        if isinstance(_unified_api_across_locations, Unset):
            unified_api_across_locations = UNSET
        else:
            unified_api_across_locations = check_provider_detail_unified_api_across_locations(
                _unified_api_across_locations
            )

        _vm_available = d.pop("vm_available", UNSET)
        vm_available: ProviderDetailVmAvailable | Unset
        if isinstance(_vm_available, Unset):
            vm_available = UNSET
        else:
            vm_available = check_provider_detail_vm_available(_vm_available)

        _dedicated_available = d.pop("dedicated_available", UNSET)
        dedicated_available: ProviderDetailDedicatedAvailable | Unset
        if isinstance(_dedicated_available, Unset):
            dedicated_available = UNSET
        else:
            dedicated_available = check_provider_detail_dedicated_available(_dedicated_available)

        _cloud_init = d.pop("cloud_init", UNSET)
        cloud_init: ProviderDetailCloudInit | Unset
        if isinstance(_cloud_init, Unset):
            cloud_init = UNSET
        else:
            cloud_init = check_provider_detail_cloud_init(_cloud_init)

        _custom_images = d.pop("custom_images", UNSET)
        custom_images: ProviderDetailCustomImages | Unset
        if isinstance(_custom_images, Unset):
            custom_images = UNSET
        else:
            custom_images = check_provider_detail_custom_images(_custom_images)

        _api_public_docs = d.pop("api_public_docs", UNSET)
        api_public_docs: ProviderDetailApiPublicDocs | Unset
        if isinstance(_api_public_docs, Unset):
            api_public_docs = UNSET
        else:
            api_public_docs = check_provider_detail_api_public_docs(_api_public_docs)

        _tenant_segmentation = d.pop("tenant_segmentation", UNSET)
        tenant_segmentation: ProviderDetailTenantSegmentation | Unset
        if isinstance(_tenant_segmentation, Unset):
            tenant_segmentation = UNSET
        else:
            tenant_segmentation = check_provider_detail_tenant_segmentation(_tenant_segmentation)

        _scoped_api_keys = d.pop("scoped_api_keys", UNSET)
        scoped_api_keys: ProviderDetailScopedApiKeys | Unset
        if isinstance(_scoped_api_keys, Unset):
            scoped_api_keys = UNSET
        else:
            scoped_api_keys = check_provider_detail_scoped_api_keys(_scoped_api_keys)

        _maintenance_api = d.pop("maintenance_api", UNSET)
        maintenance_api: ProviderDetailMaintenanceApi | Unset
        if isinstance(_maintenance_api, Unset):
            maintenance_api = UNSET
        else:
            maintenance_api = check_provider_detail_maintenance_api(_maintenance_api)

        _block_storage_status = d.pop("block_storage_status", UNSET)
        block_storage_status: ProviderDetailBlockStorageStatus | Unset
        if isinstance(_block_storage_status, Unset):
            block_storage_status = UNSET
        else:
            block_storage_status = check_provider_detail_block_storage_status(_block_storage_status)

        _maintenance_scope = d.pop("maintenance_scope", UNSET)
        maintenance_scope: ProviderDetailMaintenanceScope | Unset
        if isinstance(_maintenance_scope, Unset):
            maintenance_scope = UNSET
        else:
            maintenance_scope = check_provider_detail_maintenance_scope(_maintenance_scope)

        _billing_model = d.pop("billing_model", UNSET)
        billing_model: ProviderDetailBillingModel | Unset
        if isinstance(_billing_model, Unset):
            billing_model = UNSET
        else:
            billing_model = check_provider_detail_billing_model(_billing_model)

        _min_term = d.pop("min_term", UNSET)
        min_term: ProviderDetailMinTerm | Unset
        if isinstance(_min_term, Unset):
            min_term = UNSET
        else:
            min_term = check_provider_detail_min_term(_min_term)

        _volume_discount = d.pop("volume_discount", UNSET)
        volume_discount: ProviderDetailVolumeDiscount | Unset
        if isinstance(_volume_discount, Unset):
            volume_discount = UNSET
        else:
            volume_discount = check_provider_detail_volume_discount(_volume_discount)

        uptime_sla = d.pop("uptime_sla", UNSET)

        certification_evidence = d.pop("certification_evidence", UNSET)

        provider_detail = cls(
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
            has_icon=has_icon,
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

        provider_detail.additional_properties = d
        return provider_detail

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
