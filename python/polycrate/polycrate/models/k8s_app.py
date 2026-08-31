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
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.k8s_app_kind_enum import K8SAppKindEnum, check_k8s_app_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.k8s_app_created import K8SAppCreated
    from ..models.k8s_app_deleted_by_user_type_0 import K8SAppDeletedByUserType0
    from ..models.k8s_app_last_action_run_type_0 import K8SAppLastActionRunType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.product_simple import ProductSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="K8SApp")


@_attrs_define
class K8SApp:
    """Full serializer for K8sApp detail view.

    Attributes:
        id (UUID):
        created (K8SAppCreated):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (WorkspaceSimple):
        url (str): Gibt die absolute URL zum Object zurück.
        icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
            Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
        is_class_icon (bool):
        effective_slo_target (float | None):
        effective_sla_target (float | None):
        effective_criticality (EffectiveCriticalityEnum | None):
        last_action_run (K8SAppLastActionRunType0 | None):
        deleted_by_user (K8SAppDeletedByUserType0 | None):
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
        discovery_running (bool):
        discovery_task_id (None | str):
        discovery_task_meta (Any): Task metadata for discovery progress tracking
        last_discovery (datetime.datetime | None):
        repair_running (bool):
        repair_task_id (None | str):
        repair_task_meta (Any): Task metadata for repair progress tracking
        last_repair (datetime.datetime | None):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        tolerations (Any): Tolerations match conditions. If a toleration for a condition exists for an object, the
            condition will not be applied.
        name (str | Unset): Object name
        block (None | Unset | UUID):
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
        last_reconciliation_duration_seconds (float | None | Unset): Duration of the last reconciliation in seconds
        discovery_enabled (bool | Unset):
        scope (ScopeEnum | Unset): * `system` - System
            * `user` - User
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
        actual_availability (str | Unset): Calculated actual availability as yearly average in %
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
        kind (K8SAppKindEnum | Unset): * `helm` - Helm
            * `polycrate` - Polycrate
            * `external` - External
        description (None | str | Unset):
        active (bool | Unset):
        source (None | str | Unset):
        platform_service (bool | Unset): Makes this app available for the whole platform instead of a single
            organization
        byoa (bool | Unset): Bring-your-own app: kind=external, no Block. CatalogueApp via SystemConfig
            BYOA_CATALOGUE_APP_ID.
        namespace (None | str | Unset):
        ha_enabled (bool | None | Unset): Whether HA mode is active. Evaluated from CatalogueApp.ha_enabled_expression
            at each reconciliation. None = not yet evaluated.
        installed_version (None | str | Unset):
        installed (bool | Unset):
        uninstalled (bool | Unset):
        installation_running (bool | Unset):
        uninstallation_running (bool | Unset):
        installation_failed (bool | Unset):
        uninstallation_failed (bool | Unset):
        last_installation (datetime.datetime | None | Unset):
        last_metrics_check (datetime.datetime | None | Unset): Last time VictoriaMetrics was checked for
            replicaset/statefulset activities
        pods_total (int | Unset): Total number of pods belonging to this K8sApp
        pods_ready (int | Unset): Number of ready pods
        pods_available (int | Unset): Number of available pods (passed availability probe)
        pods_unavailable (int | Unset): Number of unavailable pods
        pods_restart_count_total (int | Unset): Total restart count across all pods/containers
        pods_restart_count_last_hour (int | Unset): Restart count in the last hour
        pods_details (Any | Unset): Detailed information about each pod (name, status, restarts, containers)
        pods_status_hash (None | str | Unset): Hash of pod status data for change detection
        pods_status_updated_at (datetime.datetime | None | Unset): Last time pod status was updated by operator
        excluded_from_downtime_until (datetime.datetime | None | Unset): Exclude this K8sApp from downtime triggers
            until this time (flapping protection)
        archived_by (int | None | Unset): The user who archived the object
        managed_by_content_type (int | None | Unset):
        modified_by_user (int | None | Unset): The user who last modified the object
        created_by_user (int | None | Unset): The user who created the object
        helm_chart (None | Unset | UUID):
        artifact_package (None | Unset | UUID):
        artifact (None | Unset | UUID):
        catalogue_app (None | Unset | UUID): Associated Catalogue App from the platform app catalogue
        k8s_cluster (None | Unset | UUID):
    """

    id: UUID
    created: K8SAppCreated
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    effective_criticality: EffectiveCriticalityEnum | None
    last_action_run: K8SAppLastActionRunType0 | None
    deleted_by_user: K8SAppDeletedByUserType0 | None
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
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    conditions: Any
    tolerations: Any
    name: str | Unset = UNSET
    block: None | Unset | UUID = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    actual_availability: str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    kind: K8SAppKindEnum | Unset = UNSET
    description: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    source: None | str | Unset = UNSET
    platform_service: bool | Unset = UNSET
    byoa: bool | Unset = UNSET
    namespace: None | str | Unset = UNSET
    ha_enabled: bool | None | Unset = UNSET
    installed_version: None | str | Unset = UNSET
    installed: bool | Unset = UNSET
    uninstalled: bool | Unset = UNSET
    installation_running: bool | Unset = UNSET
    uninstallation_running: bool | Unset = UNSET
    installation_failed: bool | Unset = UNSET
    uninstallation_failed: bool | Unset = UNSET
    last_installation: datetime.datetime | None | Unset = UNSET
    last_metrics_check: datetime.datetime | None | Unset = UNSET
    pods_total: int | Unset = UNSET
    pods_ready: int | Unset = UNSET
    pods_available: int | Unset = UNSET
    pods_unavailable: int | Unset = UNSET
    pods_restart_count_total: int | Unset = UNSET
    pods_restart_count_last_hour: int | Unset = UNSET
    pods_details: Any | Unset = UNSET
    pods_status_hash: None | str | Unset = UNSET
    pods_status_updated_at: datetime.datetime | None | Unset = UNSET
    excluded_from_downtime_until: datetime.datetime | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    helm_chart: None | Unset | UUID = UNSET
    artifact_package: None | Unset | UUID = UNSET
    artifact: None | Unset | UUID = UNSET
    catalogue_app: None | Unset | UUID = UNSET
    k8s_cluster: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_app_deleted_by_user_type_0 import K8SAppDeletedByUserType0
        from ..models.k8s_app_last_action_run_type_0 import K8SAppLastActionRunType0

        id = str(self.id)

        created = self.created.to_dict()

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

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
        if isinstance(self.last_action_run, K8SAppLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, K8SAppDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

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

        conditions = self.conditions

        tolerations = self.tolerations

        name = self.name

        block: None | str | Unset
        if isinstance(self.block, Unset):
            block = UNSET
        elif isinstance(self.block, UUID):
            block = str(self.block)
        else:
            block = self.block

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

        discovery_enabled = self.discovery_enabled

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

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

        actual_availability = self.actual_availability

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

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        active = self.active

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        platform_service = self.platform_service

        byoa = self.byoa

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        ha_enabled: bool | None | Unset
        if isinstance(self.ha_enabled, Unset):
            ha_enabled = UNSET
        else:
            ha_enabled = self.ha_enabled

        installed_version: None | str | Unset
        if isinstance(self.installed_version, Unset):
            installed_version = UNSET
        else:
            installed_version = self.installed_version

        installed = self.installed

        uninstalled = self.uninstalled

        installation_running = self.installation_running

        uninstallation_running = self.uninstallation_running

        installation_failed = self.installation_failed

        uninstallation_failed = self.uninstallation_failed

        last_installation: None | str | Unset
        if isinstance(self.last_installation, Unset):
            last_installation = UNSET
        elif isinstance(self.last_installation, datetime.datetime):
            last_installation = self.last_installation.isoformat()
        else:
            last_installation = self.last_installation

        last_metrics_check: None | str | Unset
        if isinstance(self.last_metrics_check, Unset):
            last_metrics_check = UNSET
        elif isinstance(self.last_metrics_check, datetime.datetime):
            last_metrics_check = self.last_metrics_check.isoformat()
        else:
            last_metrics_check = self.last_metrics_check

        pods_total = self.pods_total

        pods_ready = self.pods_ready

        pods_available = self.pods_available

        pods_unavailable = self.pods_unavailable

        pods_restart_count_total = self.pods_restart_count_total

        pods_restart_count_last_hour = self.pods_restart_count_last_hour

        pods_details = self.pods_details

        pods_status_hash: None | str | Unset
        if isinstance(self.pods_status_hash, Unset):
            pods_status_hash = UNSET
        else:
            pods_status_hash = self.pods_status_hash

        pods_status_updated_at: None | str | Unset
        if isinstance(self.pods_status_updated_at, Unset):
            pods_status_updated_at = UNSET
        elif isinstance(self.pods_status_updated_at, datetime.datetime):
            pods_status_updated_at = self.pods_status_updated_at.isoformat()
        else:
            pods_status_updated_at = self.pods_status_updated_at

        excluded_from_downtime_until: None | str | Unset
        if isinstance(self.excluded_from_downtime_until, Unset):
            excluded_from_downtime_until = UNSET
        elif isinstance(self.excluded_from_downtime_until, datetime.datetime):
            excluded_from_downtime_until = self.excluded_from_downtime_until.isoformat()
        else:
            excluded_from_downtime_until = self.excluded_from_downtime_until

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

        helm_chart: None | str | Unset
        if isinstance(self.helm_chart, Unset):
            helm_chart = UNSET
        elif isinstance(self.helm_chart, UUID):
            helm_chart = str(self.helm_chart)
        else:
            helm_chart = self.helm_chart

        artifact_package: None | str | Unset
        if isinstance(self.artifact_package, Unset):
            artifact_package = UNSET
        elif isinstance(self.artifact_package, UUID):
            artifact_package = str(self.artifact_package)
        else:
            artifact_package = self.artifact_package

        artifact: None | str | Unset
        if isinstance(self.artifact, Unset):
            artifact = UNSET
        elif isinstance(self.artifact, UUID):
            artifact = str(self.artifact)
        else:
            artifact = self.artifact

        catalogue_app: None | str | Unset
        if isinstance(self.catalogue_app, Unset):
            catalogue_app = UNSET
        elif isinstance(self.catalogue_app, UUID):
            catalogue_app = str(self.catalogue_app)
        else:
            catalogue_app = self.catalogue_app

        k8s_cluster: None | str | Unset
        if isinstance(self.k8s_cluster, Unset):
            k8s_cluster = UNSET
        elif isinstance(self.k8s_cluster, UUID):
            k8s_cluster = str(self.k8s_cluster)
        else:
            k8s_cluster = self.k8s_cluster

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
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "conditions": conditions,
                "tolerations": tolerations,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if block is not UNSET:
            field_dict["block"] = block
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
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if scope is not UNSET:
            field_dict["scope"] = scope
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
        if actual_availability is not UNSET:
            field_dict["actual_availability"] = actual_availability
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
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if source is not UNSET:
            field_dict["source"] = source
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if byoa is not UNSET:
            field_dict["byoa"] = byoa
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if ha_enabled is not UNSET:
            field_dict["ha_enabled"] = ha_enabled
        if installed_version is not UNSET:
            field_dict["installed_version"] = installed_version
        if installed is not UNSET:
            field_dict["installed"] = installed
        if uninstalled is not UNSET:
            field_dict["uninstalled"] = uninstalled
        if installation_running is not UNSET:
            field_dict["installation_running"] = installation_running
        if uninstallation_running is not UNSET:
            field_dict["uninstallation_running"] = uninstallation_running
        if installation_failed is not UNSET:
            field_dict["installation_failed"] = installation_failed
        if uninstallation_failed is not UNSET:
            field_dict["uninstallation_failed"] = uninstallation_failed
        if last_installation is not UNSET:
            field_dict["last_installation"] = last_installation
        if last_metrics_check is not UNSET:
            field_dict["last_metrics_check"] = last_metrics_check
        if pods_total is not UNSET:
            field_dict["pods_total"] = pods_total
        if pods_ready is not UNSET:
            field_dict["pods_ready"] = pods_ready
        if pods_available is not UNSET:
            field_dict["pods_available"] = pods_available
        if pods_unavailable is not UNSET:
            field_dict["pods_unavailable"] = pods_unavailable
        if pods_restart_count_total is not UNSET:
            field_dict["pods_restart_count_total"] = pods_restart_count_total
        if pods_restart_count_last_hour is not UNSET:
            field_dict["pods_restart_count_last_hour"] = pods_restart_count_last_hour
        if pods_details is not UNSET:
            field_dict["pods_details"] = pods_details
        if pods_status_hash is not UNSET:
            field_dict["pods_status_hash"] = pods_status_hash
        if pods_status_updated_at is not UNSET:
            field_dict["pods_status_updated_at"] = pods_status_updated_at
        if excluded_from_downtime_until is not UNSET:
            field_dict["excluded_from_downtime_until"] = excluded_from_downtime_until
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if helm_chart is not UNSET:
            field_dict["helm_chart"] = helm_chart
        if artifact_package is not UNSET:
            field_dict["artifact_package"] = artifact_package
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if catalogue_app is not UNSET:
            field_dict["catalogue_app"] = catalogue_app
        if k8s_cluster is not UNSET:
            field_dict["k8s_cluster"] = k8s_cluster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_app_created import K8SAppCreated
        from ..models.k8s_app_deleted_by_user_type_0 import K8SAppDeletedByUserType0
        from ..models.k8s_app_last_action_run_type_0 import K8SAppLastActionRunType0
        from ..models.organization_simple import OrganizationSimple
        from ..models.product_simple import ProductSimple
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = K8SAppCreated.from_dict(d.pop("created"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

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

        def _parse_last_action_run(data: object) -> K8SAppLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = K8SAppLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_deleted_by_user(data: object) -> K8SAppDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = K8SAppDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SAppDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

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

        conditions = d.pop("conditions")

        tolerations = d.pop("tolerations")

        name = d.pop("name", UNSET)

        def _parse_block(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                block_type_0 = UUID(data)

                return block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        block = _parse_block(d.pop("block", UNSET))

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

        def _parse_last_reconciliation_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_reconciliation_duration_seconds = _parse_last_reconciliation_duration_seconds(
            d.pop("last_reconciliation_duration_seconds", UNSET)
        )

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

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

        actual_availability = d.pop("actual_availability", UNSET)

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
        kind: K8SAppKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_k8s_app_kind_enum(_kind)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        active = d.pop("active", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        platform_service = d.pop("platform_service", UNSET)

        byoa = d.pop("byoa", UNSET)

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_ha_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ha_enabled = _parse_ha_enabled(d.pop("ha_enabled", UNSET))

        def _parse_installed_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installed_version = _parse_installed_version(d.pop("installed_version", UNSET))

        installed = d.pop("installed", UNSET)

        uninstalled = d.pop("uninstalled", UNSET)

        installation_running = d.pop("installation_running", UNSET)

        uninstallation_running = d.pop("uninstallation_running", UNSET)

        installation_failed = d.pop("installation_failed", UNSET)

        uninstallation_failed = d.pop("uninstallation_failed", UNSET)

        def _parse_last_installation(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_installation_type_0 = datetime.datetime.fromisoformat(data)

                return last_installation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_installation = _parse_last_installation(d.pop("last_installation", UNSET))

        def _parse_last_metrics_check(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_metrics_check_type_0 = datetime.datetime.fromisoformat(data)

                return last_metrics_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_metrics_check = _parse_last_metrics_check(d.pop("last_metrics_check", UNSET))

        pods_total = d.pop("pods_total", UNSET)

        pods_ready = d.pop("pods_ready", UNSET)

        pods_available = d.pop("pods_available", UNSET)

        pods_unavailable = d.pop("pods_unavailable", UNSET)

        pods_restart_count_total = d.pop("pods_restart_count_total", UNSET)

        pods_restart_count_last_hour = d.pop("pods_restart_count_last_hour", UNSET)

        pods_details = d.pop("pods_details", UNSET)

        def _parse_pods_status_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pods_status_hash = _parse_pods_status_hash(d.pop("pods_status_hash", UNSET))

        def _parse_pods_status_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pods_status_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return pods_status_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pods_status_updated_at = _parse_pods_status_updated_at(d.pop("pods_status_updated_at", UNSET))

        def _parse_excluded_from_downtime_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                excluded_from_downtime_until_type_0 = datetime.datetime.fromisoformat(data)

                return excluded_from_downtime_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        excluded_from_downtime_until = _parse_excluded_from_downtime_until(d.pop("excluded_from_downtime_until", UNSET))

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

        def _parse_helm_chart(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                helm_chart_type_0 = UUID(data)

                return helm_chart_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        helm_chart = _parse_helm_chart(d.pop("helm_chart", UNSET))

        def _parse_artifact_package(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                artifact_package_type_0 = UUID(data)

                return artifact_package_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        artifact_package = _parse_artifact_package(d.pop("artifact_package", UNSET))

        def _parse_artifact(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                artifact_type_0 = UUID(data)

                return artifact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        artifact = _parse_artifact(d.pop("artifact", UNSET))

        def _parse_catalogue_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                catalogue_app_type_0 = UUID(data)

                return catalogue_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        catalogue_app = _parse_catalogue_app(d.pop("catalogue_app", UNSET))

        def _parse_k8s_cluster(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_cluster_type_0 = UUID(data)

                return k8s_cluster_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        k8s_cluster = _parse_k8s_cluster(d.pop("k8s_cluster", UNSET))

        k8s_app = cls(
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
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            conditions=conditions,
            tolerations=tolerations,
            name=name,
            block=block,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            discovery_enabled=discovery_enabled,
            scope=scope,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            created_by_component=created_by_component,
            target_availability=target_availability,
            actual_availability=actual_availability,
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
            description=description,
            active=active,
            source=source,
            platform_service=platform_service,
            byoa=byoa,
            namespace=namespace,
            ha_enabled=ha_enabled,
            installed_version=installed_version,
            installed=installed,
            uninstalled=uninstalled,
            installation_running=installation_running,
            uninstallation_running=uninstallation_running,
            installation_failed=installation_failed,
            uninstallation_failed=uninstallation_failed,
            last_installation=last_installation,
            last_metrics_check=last_metrics_check,
            pods_total=pods_total,
            pods_ready=pods_ready,
            pods_available=pods_available,
            pods_unavailable=pods_unavailable,
            pods_restart_count_total=pods_restart_count_total,
            pods_restart_count_last_hour=pods_restart_count_last_hour,
            pods_details=pods_details,
            pods_status_hash=pods_status_hash,
            pods_status_updated_at=pods_status_updated_at,
            excluded_from_downtime_until=excluded_from_downtime_until,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            helm_chart=helm_chart,
            artifact_package=artifact_package,
            artifact=artifact,
            catalogue_app=catalogue_app,
            k8s_cluster=k8s_cluster,
        )

        k8s_app.additional_properties = d
        return k8s_app

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
