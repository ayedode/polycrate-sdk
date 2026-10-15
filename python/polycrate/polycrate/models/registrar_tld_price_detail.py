from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.registrar_tld_price_detail_created_by_component_type_1 import (
    RegistrarTLDPriceDetailCreatedByComponentType1,
    check_registrar_tld_price_detail_created_by_component_type_1,
)
from ..models.registrar_tld_price_detail_created_by_component_type_2_type_1 import (
    RegistrarTLDPriceDetailCreatedByComponentType2Type1,
    check_registrar_tld_price_detail_created_by_component_type_2_type_1,
)
from ..models.registrar_tld_price_detail_created_by_component_type_3_type_1 import (
    RegistrarTLDPriceDetailCreatedByComponentType3Type1,
    check_registrar_tld_price_detail_created_by_component_type_3_type_1,
)
from ..models.registrar_tld_price_detail_criticality_type_1 import (
    RegistrarTLDPriceDetailCriticalityType1,
    check_registrar_tld_price_detail_criticality_type_1,
)
from ..models.registrar_tld_price_detail_criticality_type_2_type_1 import (
    RegistrarTLDPriceDetailCriticalityType2Type1,
    check_registrar_tld_price_detail_criticality_type_2_type_1,
)
from ..models.registrar_tld_price_detail_criticality_type_3_type_1 import (
    RegistrarTLDPriceDetailCriticalityType3Type1,
    check_registrar_tld_price_detail_criticality_type_3_type_1,
)
from ..models.registrar_tld_price_detail_effective_criticality_type_1 import (
    RegistrarTLDPriceDetailEffectiveCriticalityType1,
    check_registrar_tld_price_detail_effective_criticality_type_1,
)
from ..models.registrar_tld_price_detail_effective_criticality_type_2_type_1 import (
    RegistrarTLDPriceDetailEffectiveCriticalityType2Type1,
    check_registrar_tld_price_detail_effective_criticality_type_2_type_1,
)
from ..models.registrar_tld_price_detail_effective_criticality_type_3_type_1 import (
    RegistrarTLDPriceDetailEffectiveCriticalityType3Type1,
    check_registrar_tld_price_detail_effective_criticality_type_3_type_1,
)
from ..models.registrar_tld_price_detail_kind import RegistrarTLDPriceDetailKind, check_registrar_tld_price_detail_kind
from ..models.registrar_tld_price_detail_last_state import (
    RegistrarTLDPriceDetailLastState,
    check_registrar_tld_price_detail_last_state,
)
from ..models.registrar_tld_price_detail_provider import (
    RegistrarTLDPriceDetailProvider,
    check_registrar_tld_price_detail_provider,
)
from ..models.registrar_tld_price_detail_scope import (
    RegistrarTLDPriceDetailScope,
    check_registrar_tld_price_detail_scope,
)
from ..models.registrar_tld_price_detail_state import (
    RegistrarTLDPriceDetailState,
    check_registrar_tld_price_detail_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_registrar_simple import DomainRegistrarSimple
    from ..models.registrar_tld_price_detail_created import RegistrarTLDPriceDetailCreated
    from ..models.registrar_tld_price_detail_deleted_by_user_type_0 import RegistrarTLDPriceDetailDeletedByUserType0
    from ..models.registrar_tld_price_detail_last_action_run_type_0 import RegistrarTLDPriceDetailLastActionRunType0
    from ..models.registrar_tld_price_detail_organization_type_0 import RegistrarTLDPriceDetailOrganizationType0
    from ..models.registrar_tld_price_detail_workspace_type_0 import RegistrarTLDPriceDetailWorkspaceType0


T = TypeVar("T", bound="RegistrarTLDPriceDetail")


@_attrs_define
class RegistrarTLDPriceDetail:
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
            created (RegistrarTLDPriceDetailCreated):
            organization (None | RegistrarTLDPriceDetailOrganizationType0):
            workspace (None | RegistrarTLDPriceDetailWorkspaceType0):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            effective_criticality (None | RegistrarTLDPriceDetailEffectiveCriticalityType1 |
                RegistrarTLDPriceDetailEffectiveCriticalityType2Type1 | RegistrarTLDPriceDetailEffectiveCriticalityType3Type1):
            last_action_run (None | RegistrarTLDPriceDetailLastActionRunType0):
            deleted_by_user (None | RegistrarTLDPriceDetailDeletedByUserType0):
            registrar (DomainRegistrarSimple):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            state (RegistrarTLDPriceDetailState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (RegistrarTLDPriceDetailLastState): * `OK` - Ok
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
            scope (RegistrarTLDPriceDetailScope): The scope is used to separate `system` owned objects from `user` owned
                objects.

                * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            actual_availability (str): Calculated actual availability as yearly average in %
            tld (str): TLD without leading dot.
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (RegistrarTLDPriceDetailProvider | Unset): * `loopback` - Loopback
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
            last_reconciliation_duration_seconds (float | None | Unset): Duration of the last reconciliation in seconds
            platform_service (bool | Unset):
            kind (RegistrarTLDPriceDetailKind | Unset): * `generic` - Generic
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            created_by_component (None | RegistrarTLDPriceDetailCreatedByComponentType1 |
                RegistrarTLDPriceDetailCreatedByComponentType2Type1 | RegistrarTLDPriceDetailCreatedByComponentType3Type1 |
                Unset): Component that created this object: cli, operator, or api.

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
            criticality (None | RegistrarTLDPriceDetailCriticalityType1 | RegistrarTLDPriceDetailCriticalityType2Type1 |
                RegistrarTLDPriceDetailCriticalityType3Type1 | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            managed_by_object_id (None | str | Unset):
            platform_dns_record_created (bool | Unset):
            provider_status (str | Unset):
            active (bool | Unset): Staff switch: we sell this TLD. Sync never writes this field.
            offerable (bool | Unset): Informative OpenProvider list flag. Not the sales filter.
            domicile_available (bool | Unset):
            transfer_available (bool | Unset):
            trade_available (bool | Unset):
            renew_available (bool | Unset):
            private_whois_allowed (bool | Unset):
            min_period (int | None | Unset):
            max_period (int | None | Unset):
            currency (str | Unset):
            ek_create (None | str | Unset):
            ek_renew (None | str | Unset):
            ek_transfer (None | str | Unset):
            ek_restore (None | str | Unset):
            ek_soft_restore (None | str | Unset):
            ek_setup (None | str | Unset):
            ek_update (None | str | Unset):
            ek_trade (None | str | Unset):
            ek_domicile (None | str | Unset):
            vk_create (None | str | Unset):
            vk_renew (None | str | Unset):
            vk_transfer (None | str | Unset):
            vk_domicile (None | str | Unset):
            prices_extra (Any | Unset):
            last_ek_synced_at (datetime.datetime | None | Unset):
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
    """

    id: UUID
    created: RegistrarTLDPriceDetailCreated
    organization: None | RegistrarTLDPriceDetailOrganizationType0
    workspace: None | RegistrarTLDPriceDetailWorkspaceType0
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    effective_criticality: (
        None
        | RegistrarTLDPriceDetailEffectiveCriticalityType1
        | RegistrarTLDPriceDetailEffectiveCriticalityType2Type1
        | RegistrarTLDPriceDetailEffectiveCriticalityType3Type1
    )
    last_action_run: None | RegistrarTLDPriceDetailLastActionRunType0
    deleted_by_user: None | RegistrarTLDPriceDetailDeletedByUserType0
    registrar: DomainRegistrarSimple
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    state: RegistrarTLDPriceDetailState
    state_reason: None | str
    last_state: RegistrarTLDPriceDetailLastState
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
    scope: RegistrarTLDPriceDetailScope
    conditions: Any
    actual_availability: str
    tld: str
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: RegistrarTLDPriceDetailProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: RegistrarTLDPriceDetailKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: (
        None
        | RegistrarTLDPriceDetailCreatedByComponentType1
        | RegistrarTLDPriceDetailCreatedByComponentType2Type1
        | RegistrarTLDPriceDetailCreatedByComponentType3Type1
        | Unset
    ) = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: (
        None
        | RegistrarTLDPriceDetailCriticalityType1
        | RegistrarTLDPriceDetailCriticalityType2Type1
        | RegistrarTLDPriceDetailCriticalityType3Type1
        | Unset
    ) = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    provider_status: str | Unset = UNSET
    active: bool | Unset = UNSET
    offerable: bool | Unset = UNSET
    domicile_available: bool | Unset = UNSET
    transfer_available: bool | Unset = UNSET
    trade_available: bool | Unset = UNSET
    renew_available: bool | Unset = UNSET
    private_whois_allowed: bool | Unset = UNSET
    min_period: int | None | Unset = UNSET
    max_period: int | None | Unset = UNSET
    currency: str | Unset = UNSET
    ek_create: None | str | Unset = UNSET
    ek_renew: None | str | Unset = UNSET
    ek_transfer: None | str | Unset = UNSET
    ek_restore: None | str | Unset = UNSET
    ek_soft_restore: None | str | Unset = UNSET
    ek_setup: None | str | Unset = UNSET
    ek_update: None | str | Unset = UNSET
    ek_trade: None | str | Unset = UNSET
    ek_domicile: None | str | Unset = UNSET
    vk_create: None | str | Unset = UNSET
    vk_renew: None | str | Unset = UNSET
    vk_transfer: None | str | Unset = UNSET
    vk_domicile: None | str | Unset = UNSET
    prices_extra: Any | Unset = UNSET
    last_ek_synced_at: datetime.datetime | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.registrar_tld_price_detail_deleted_by_user_type_0 import RegistrarTLDPriceDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_last_action_run_type_0 import RegistrarTLDPriceDetailLastActionRunType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_organization_type_0 import RegistrarTLDPriceDetailOrganizationType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_workspace_type_0 import RegistrarTLDPriceDetailWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        created = self.created.to_dict()

        organization: dict[str, Any] | None
        if isinstance(self.organization, RegistrarTLDPriceDetailOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, RegistrarTLDPriceDetailWorkspaceType0):
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
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, RegistrarTLDPriceDetailLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, RegistrarTLDPriceDetailDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        registrar = self.registrar.to_dict()

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

        tld = self.tld

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

        last_reconciliation_duration_seconds: float | None | Unset
        if isinstance(self.last_reconciliation_duration_seconds, Unset):
            last_reconciliation_duration_seconds = UNSET
        else:
            last_reconciliation_duration_seconds = self.last_reconciliation_duration_seconds

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

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
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

        provider_status = self.provider_status

        active = self.active

        offerable = self.offerable

        domicile_available = self.domicile_available

        transfer_available = self.transfer_available

        trade_available = self.trade_available

        renew_available = self.renew_available

        private_whois_allowed = self.private_whois_allowed

        min_period: int | None | Unset
        if isinstance(self.min_period, Unset):
            min_period = UNSET
        else:
            min_period = self.min_period

        max_period: int | None | Unset
        if isinstance(self.max_period, Unset):
            max_period = UNSET
        else:
            max_period = self.max_period

        currency = self.currency

        ek_create: None | str | Unset
        if isinstance(self.ek_create, Unset):
            ek_create = UNSET
        else:
            ek_create = self.ek_create

        ek_renew: None | str | Unset
        if isinstance(self.ek_renew, Unset):
            ek_renew = UNSET
        else:
            ek_renew = self.ek_renew

        ek_transfer: None | str | Unset
        if isinstance(self.ek_transfer, Unset):
            ek_transfer = UNSET
        else:
            ek_transfer = self.ek_transfer

        ek_restore: None | str | Unset
        if isinstance(self.ek_restore, Unset):
            ek_restore = UNSET
        else:
            ek_restore = self.ek_restore

        ek_soft_restore: None | str | Unset
        if isinstance(self.ek_soft_restore, Unset):
            ek_soft_restore = UNSET
        else:
            ek_soft_restore = self.ek_soft_restore

        ek_setup: None | str | Unset
        if isinstance(self.ek_setup, Unset):
            ek_setup = UNSET
        else:
            ek_setup = self.ek_setup

        ek_update: None | str | Unset
        if isinstance(self.ek_update, Unset):
            ek_update = UNSET
        else:
            ek_update = self.ek_update

        ek_trade: None | str | Unset
        if isinstance(self.ek_trade, Unset):
            ek_trade = UNSET
        else:
            ek_trade = self.ek_trade

        ek_domicile: None | str | Unset
        if isinstance(self.ek_domicile, Unset):
            ek_domicile = UNSET
        else:
            ek_domicile = self.ek_domicile

        vk_create: None | str | Unset
        if isinstance(self.vk_create, Unset):
            vk_create = UNSET
        else:
            vk_create = self.vk_create

        vk_renew: None | str | Unset
        if isinstance(self.vk_renew, Unset):
            vk_renew = UNSET
        else:
            vk_renew = self.vk_renew

        vk_transfer: None | str | Unset
        if isinstance(self.vk_transfer, Unset):
            vk_transfer = UNSET
        else:
            vk_transfer = self.vk_transfer

        vk_domicile: None | str | Unset
        if isinstance(self.vk_domicile, Unset):
            vk_domicile = UNSET
        else:
            vk_domicile = self.vk_domicile

        prices_extra = self.prices_extra

        last_ek_synced_at: None | str | Unset
        if isinstance(self.last_ek_synced_at, Unset):
            last_ek_synced_at = UNSET
        elif isinstance(self.last_ek_synced_at, datetime.datetime):
            last_ek_synced_at = self.last_ek_synced_at.isoformat()
        else:
            last_ek_synced_at = self.last_ek_synced_at

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
                "registrar": registrar,
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
                "tld": tld,
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
        if last_reconciliation_duration_seconds is not UNSET:
            field_dict["last_reconciliation_duration_seconds"] = last_reconciliation_duration_seconds
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
        if provider_status is not UNSET:
            field_dict["provider_status"] = provider_status
        if active is not UNSET:
            field_dict["active"] = active
        if offerable is not UNSET:
            field_dict["offerable"] = offerable
        if domicile_available is not UNSET:
            field_dict["domicile_available"] = domicile_available
        if transfer_available is not UNSET:
            field_dict["transfer_available"] = transfer_available
        if trade_available is not UNSET:
            field_dict["trade_available"] = trade_available
        if renew_available is not UNSET:
            field_dict["renew_available"] = renew_available
        if private_whois_allowed is not UNSET:
            field_dict["private_whois_allowed"] = private_whois_allowed
        if min_period is not UNSET:
            field_dict["min_period"] = min_period
        if max_period is not UNSET:
            field_dict["max_period"] = max_period
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ek_create is not UNSET:
            field_dict["ek_create"] = ek_create
        if ek_renew is not UNSET:
            field_dict["ek_renew"] = ek_renew
        if ek_transfer is not UNSET:
            field_dict["ek_transfer"] = ek_transfer
        if ek_restore is not UNSET:
            field_dict["ek_restore"] = ek_restore
        if ek_soft_restore is not UNSET:
            field_dict["ek_soft_restore"] = ek_soft_restore
        if ek_setup is not UNSET:
            field_dict["ek_setup"] = ek_setup
        if ek_update is not UNSET:
            field_dict["ek_update"] = ek_update
        if ek_trade is not UNSET:
            field_dict["ek_trade"] = ek_trade
        if ek_domicile is not UNSET:
            field_dict["ek_domicile"] = ek_domicile
        if vk_create is not UNSET:
            field_dict["vk_create"] = vk_create
        if vk_renew is not UNSET:
            field_dict["vk_renew"] = vk_renew
        if vk_transfer is not UNSET:
            field_dict["vk_transfer"] = vk_transfer
        if vk_domicile is not UNSET:
            field_dict["vk_domicile"] = vk_domicile
        if prices_extra is not UNSET:
            field_dict["prices_extra"] = prices_extra
        if last_ek_synced_at is not UNSET:
            field_dict["last_ek_synced_at"] = last_ek_synced_at
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_registrar_simple import DomainRegistrarSimple  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_created import RegistrarTLDPriceDetailCreated  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_deleted_by_user_type_0 import RegistrarTLDPriceDetailDeletedByUserType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_last_action_run_type_0 import RegistrarTLDPriceDetailLastActionRunType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_organization_type_0 import RegistrarTLDPriceDetailOrganizationType0  # noqa: PLC0415
        from ..models.registrar_tld_price_detail_workspace_type_0 import RegistrarTLDPriceDetailWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = RegistrarTLDPriceDetailCreated.from_dict(d.pop("created"))

        def _parse_organization(data: object) -> None | RegistrarTLDPriceDetailOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = RegistrarTLDPriceDetailOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceDetailOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> None | RegistrarTLDPriceDetailWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = RegistrarTLDPriceDetailWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceDetailWorkspaceType0, data)

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

        def _parse_effective_criticality(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceDetailEffectiveCriticalityType1
            | RegistrarTLDPriceDetailEffectiveCriticalityType2Type1
            | RegistrarTLDPriceDetailEffectiveCriticalityType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_registrar_tld_price_detail_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = (
                    check_registrar_tld_price_detail_effective_criticality_type_2_type_1(data)
                )

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = (
                    check_registrar_tld_price_detail_effective_criticality_type_3_type_1(data)
                )

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceDetailEffectiveCriticalityType1
                | RegistrarTLDPriceDetailEffectiveCriticalityType2Type1
                | RegistrarTLDPriceDetailEffectiveCriticalityType3Type1,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        def _parse_last_action_run(data: object) -> None | RegistrarTLDPriceDetailLastActionRunType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = RegistrarTLDPriceDetailLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceDetailLastActionRunType0, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_deleted_by_user(data: object) -> None | RegistrarTLDPriceDetailDeletedByUserType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = RegistrarTLDPriceDetailDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceDetailDeletedByUserType0, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        registrar = DomainRegistrarSimple.from_dict(d.pop("registrar"))

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

        state = check_registrar_tld_price_detail_state(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_registrar_tld_price_detail_last_state(d.pop("last_state"))

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

        scope = check_registrar_tld_price_detail_scope(d.pop("scope"))

        conditions = d.pop("conditions")

        actual_availability = d.pop("actual_availability")

        tld = d.pop("tld")

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
        provider: RegistrarTLDPriceDetailProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_registrar_tld_price_detail_provider(_provider)

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

        _kind = d.pop("kind", UNSET)
        kind: RegistrarTLDPriceDetailKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_registrar_tld_price_detail_kind(_kind)

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

        def _parse_created_by_component(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceDetailCreatedByComponentType1
            | RegistrarTLDPriceDetailCreatedByComponentType2Type1
            | RegistrarTLDPriceDetailCreatedByComponentType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_registrar_tld_price_detail_created_by_component_type_1(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_2_type_1 = (
                    check_registrar_tld_price_detail_created_by_component_type_2_type_1(data)
                )

                return created_by_component_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_3_type_1 = (
                    check_registrar_tld_price_detail_created_by_component_type_3_type_1(data)
                )

                return created_by_component_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceDetailCreatedByComponentType1
                | RegistrarTLDPriceDetailCreatedByComponentType2Type1
                | RegistrarTLDPriceDetailCreatedByComponentType3Type1
                | Unset,
                data,
            )

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

        def _parse_criticality(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceDetailCriticalityType1
            | RegistrarTLDPriceDetailCriticalityType2Type1
            | RegistrarTLDPriceDetailCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_registrar_tld_price_detail_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_registrar_tld_price_detail_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_registrar_tld_price_detail_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceDetailCriticalityType1
                | RegistrarTLDPriceDetailCriticalityType2Type1
                | RegistrarTLDPriceDetailCriticalityType3Type1
                | Unset,
                data,
            )

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        provider_status = d.pop("provider_status", UNSET)

        active = d.pop("active", UNSET)

        offerable = d.pop("offerable", UNSET)

        domicile_available = d.pop("domicile_available", UNSET)

        transfer_available = d.pop("transfer_available", UNSET)

        trade_available = d.pop("trade_available", UNSET)

        renew_available = d.pop("renew_available", UNSET)

        private_whois_allowed = d.pop("private_whois_allowed", UNSET)

        def _parse_min_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_period = _parse_min_period(d.pop("min_period", UNSET))

        def _parse_max_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_period = _parse_max_period(d.pop("max_period", UNSET))

        currency = d.pop("currency", UNSET)

        def _parse_ek_create(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_create = _parse_ek_create(d.pop("ek_create", UNSET))

        def _parse_ek_renew(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_renew = _parse_ek_renew(d.pop("ek_renew", UNSET))

        def _parse_ek_transfer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_transfer = _parse_ek_transfer(d.pop("ek_transfer", UNSET))

        def _parse_ek_restore(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_restore = _parse_ek_restore(d.pop("ek_restore", UNSET))

        def _parse_ek_soft_restore(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_soft_restore = _parse_ek_soft_restore(d.pop("ek_soft_restore", UNSET))

        def _parse_ek_setup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_setup = _parse_ek_setup(d.pop("ek_setup", UNSET))

        def _parse_ek_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_update = _parse_ek_update(d.pop("ek_update", UNSET))

        def _parse_ek_trade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_trade = _parse_ek_trade(d.pop("ek_trade", UNSET))

        def _parse_ek_domicile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_domicile = _parse_ek_domicile(d.pop("ek_domicile", UNSET))

        def _parse_vk_create(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_create = _parse_vk_create(d.pop("vk_create", UNSET))

        def _parse_vk_renew(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_renew = _parse_vk_renew(d.pop("vk_renew", UNSET))

        def _parse_vk_transfer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_transfer = _parse_vk_transfer(d.pop("vk_transfer", UNSET))

        def _parse_vk_domicile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_domicile = _parse_vk_domicile(d.pop("vk_domicile", UNSET))

        prices_extra = d.pop("prices_extra", UNSET)

        def _parse_last_ek_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_ek_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_ek_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_ek_synced_at = _parse_last_ek_synced_at(d.pop("last_ek_synced_at", UNSET))

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

        registrar_tld_price_detail = cls(
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
            registrar=registrar,
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
            tld=tld,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            platform_service=platform_service,
            kind=kind,
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
            provider_status=provider_status,
            active=active,
            offerable=offerable,
            domicile_available=domicile_available,
            transfer_available=transfer_available,
            trade_available=trade_available,
            renew_available=renew_available,
            private_whois_allowed=private_whois_allowed,
            min_period=min_period,
            max_period=max_period,
            currency=currency,
            ek_create=ek_create,
            ek_renew=ek_renew,
            ek_transfer=ek_transfer,
            ek_restore=ek_restore,
            ek_soft_restore=ek_soft_restore,
            ek_setup=ek_setup,
            ek_update=ek_update,
            ek_trade=ek_trade,
            ek_domicile=ek_domicile,
            vk_create=vk_create,
            vk_renew=vk_renew,
            vk_transfer=vk_transfer,
            vk_domicile=vk_domicile,
            prices_extra=prices_extra,
            last_ek_synced_at=last_ek_synced_at,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
        )

        registrar_tld_price_detail.additional_properties = d
        return registrar_tld_price_detail

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
