from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.k8s_cluster_kind_enum import K8SClusterKindEnum, check_k8s_cluster_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.block_simple import BlockSimple
    from ..models.k8s_app_list import K8SAppList
    from ..models.k8s_cluster_created import K8SClusterCreated
    from ..models.k8s_cluster_deleted_by_user_type_0 import K8SClusterDeletedByUserType0
    from ..models.k8s_cluster_last_action_run_type_0 import K8SClusterLastActionRunType0
    from ..models.k8s_cluster_organization_type_0 import K8SClusterOrganizationType0
    from ..models.k8s_cluster_workspace_type_0 import K8SClusterWorkspaceType0
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="K8SCluster")


@_attrs_define
class K8SCluster:
    """K8sCluster Detail Serializer - erbt von ManagedObjectDetailSerializer.

    Generische Felder (von ManagedObjectDetailSerializer):
    - Alle BaseObject Felder (id, name, display_name, labels, etc.)
    - Alle ManagedObject Felder (state, reconciliation, discovery, etc.)
    - organization, workspace als generische Referenzen (mit URL)
    - created (Kombifeld), url

    K8sCluster-spezifische Felder:
    - kubernetes_version, block, kubernetes_apps, etc.

    Per .specs/0.11.4/dynamic-table-v2.md

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (K8SClusterDeletedByUserType0 | None):
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
            kind (K8SClusterKindEnum): * `polycrate` - Polycrate
                * `generic` - Generic
                * `loopback` - Loopback
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            tolerations (Any): Tolerations match conditions. If a toleration for a condition exists for an object, the
                condition will not be applied.
            effective_criticality (EffectiveCriticalityEnum | None):
            organization (K8SClusterOrganizationType0 | None):
            workspace (K8SClusterWorkspaceType0 | None):
            created (K8SClusterCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (K8SClusterLastActionRunType0 | None):
            block (BlockSimple):
            kubernetes_apps (list[K8SAppList]):
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            computed_cost (float):
            cluster_domain (None | str):
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
            discovery_enabled (bool | Unset):
            platform_service (bool | Unset):
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
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
            kubernetes_version (None | str | Unset):
            installed (bool | Unset):
            is_host_cluster (bool | Unset):
            is_infrastructure_cluster (bool | Unset):
            kubeconfig_ca_cert_expiry_date (datetime.datetime | None | Unset):
            kubeconfig_client_cert_expiry_date (datetime.datetime | None | Unset):
            api_server_cert_expiry_date (datetime.datetime | None | Unset):
            credential (None | Unset | UUID):
            discovery_ignored_namespaces (Any | Unset): Namespaces to ignore for discovery
            operator_loglevel (Any | Unset): Operator loglevel override (1=Info, 2=Debug, 3=Trace). Null = SystemConfig
                default.
            operator_ignore_namespaces (Any | Unset): List of namespaces the operator ignores for discovery. Null =
                SystemConfig default.
            alias (None | str | Unset):
            description (None | str | Unset):
            addons (Any | Unset):
            active (bool | Unset):
            backup_schedules (Any | Unset): List of backup schedules (from various providers: Velero, CloudnativePG, etc.)
            baserow_id (int | None | Unset):
            gitlab_project_id (int | None | Unset):
            last_backup_import (datetime.datetime | None | Unset): Timestamp of last backup import (for reference only, uses
                24h window)
            platform_dns_record_created (bool | Unset):
            slug (None | str | Unset):
            managed_by_content_type (int | None | Unset):
            managed_by_object_id (None | str | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: K8SClusterDeletedByUserType0 | None
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
    kind: K8SClusterKindEnum
    conditions: Any
    tolerations: Any
    effective_criticality: EffectiveCriticalityEnum | None
    organization: K8SClusterOrganizationType0 | None
    workspace: K8SClusterWorkspaceType0 | None
    created: K8SClusterCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: K8SClusterLastActionRunType0 | None
    block: BlockSimple
    kubernetes_apps: list[K8SAppList]
    product: ProductSimple
    computed_cost: float
    cluster_domain: None | str
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
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
    kubernetes_version: None | str | Unset = UNSET
    installed: bool | Unset = UNSET
    is_host_cluster: bool | Unset = UNSET
    is_infrastructure_cluster: bool | Unset = UNSET
    kubeconfig_ca_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    kubeconfig_client_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    api_server_cert_expiry_date: datetime.datetime | None | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    discovery_ignored_namespaces: Any | Unset = UNSET
    operator_loglevel: Any | Unset = UNSET
    operator_ignore_namespaces: Any | Unset = UNSET
    alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    addons: Any | Unset = UNSET
    active: bool | Unset = UNSET
    backup_schedules: Any | Unset = UNSET
    baserow_id: int | None | Unset = UNSET
    gitlab_project_id: int | None | Unset = UNSET
    last_backup_import: datetime.datetime | None | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    slug: None | str | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_cluster_deleted_by_user_type_0 import K8SClusterDeletedByUserType0  # noqa: PLC0415
        from ..models.k8s_cluster_last_action_run_type_0 import K8SClusterLastActionRunType0  # noqa: PLC0415
        from ..models.k8s_cluster_organization_type_0 import K8SClusterOrganizationType0  # noqa: PLC0415
        from ..models.k8s_cluster_workspace_type_0 import K8SClusterWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, K8SClusterDeletedByUserType0):
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

        kind: str = self.kind

        conditions = self.conditions

        tolerations = self.tolerations

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        organization: dict[str, Any] | None
        if isinstance(self.organization, K8SClusterOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SClusterWorkspaceType0):
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
        if isinstance(self.last_action_run, K8SClusterLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        block = self.block.to_dict()

        kubernetes_apps = []
        for kubernetes_apps_item_data in self.kubernetes_apps:
            kubernetes_apps_item = kubernetes_apps_item_data.to_dict()
            kubernetes_apps.append(kubernetes_apps_item)

        product = self.product.to_dict()

        computed_cost = self.computed_cost

        cluster_domain: None | str
        cluster_domain = self.cluster_domain

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

        discovery_enabled = self.discovery_enabled

        platform_service = self.platform_service

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

        kubernetes_version: None | str | Unset
        if isinstance(self.kubernetes_version, Unset):
            kubernetes_version = UNSET
        else:
            kubernetes_version = self.kubernetes_version

        installed = self.installed

        is_host_cluster = self.is_host_cluster

        is_infrastructure_cluster = self.is_infrastructure_cluster

        kubeconfig_ca_cert_expiry_date: None | str | Unset
        if isinstance(self.kubeconfig_ca_cert_expiry_date, Unset):
            kubeconfig_ca_cert_expiry_date = UNSET
        elif isinstance(self.kubeconfig_ca_cert_expiry_date, datetime.datetime):
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date.isoformat()
        else:
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date

        kubeconfig_client_cert_expiry_date: None | str | Unset
        if isinstance(self.kubeconfig_client_cert_expiry_date, Unset):
            kubeconfig_client_cert_expiry_date = UNSET
        elif isinstance(self.kubeconfig_client_cert_expiry_date, datetime.datetime):
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date.isoformat()
        else:
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date

        api_server_cert_expiry_date: None | str | Unset
        if isinstance(self.api_server_cert_expiry_date, Unset):
            api_server_cert_expiry_date = UNSET
        elif isinstance(self.api_server_cert_expiry_date, datetime.datetime):
            api_server_cert_expiry_date = self.api_server_cert_expiry_date.isoformat()
        else:
            api_server_cert_expiry_date = self.api_server_cert_expiry_date

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        discovery_ignored_namespaces = self.discovery_ignored_namespaces

        operator_loglevel = self.operator_loglevel

        operator_ignore_namespaces = self.operator_ignore_namespaces

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        addons = self.addons

        active = self.active

        backup_schedules = self.backup_schedules

        baserow_id: int | None | Unset
        if isinstance(self.baserow_id, Unset):
            baserow_id = UNSET
        else:
            baserow_id = self.baserow_id

        gitlab_project_id: int | None | Unset
        if isinstance(self.gitlab_project_id, Unset):
            gitlab_project_id = UNSET
        else:
            gitlab_project_id = self.gitlab_project_id

        last_backup_import: None | str | Unset
        if isinstance(self.last_backup_import, Unset):
            last_backup_import = UNSET
        elif isinstance(self.last_backup_import, datetime.datetime):
            last_backup_import = self.last_backup_import.isoformat()
        else:
            last_backup_import = self.last_backup_import

        platform_dns_record_created = self.platform_dns_record_created

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        managed_by_content_type: int | None | Unset
        if isinstance(self.managed_by_content_type, Unset):
            managed_by_content_type = UNSET
        else:
            managed_by_content_type = self.managed_by_content_type

        managed_by_object_id: None | str | Unset
        if isinstance(self.managed_by_object_id, Unset):
            managed_by_object_id = UNSET
        else:
            managed_by_object_id = self.managed_by_object_id

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
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "kind": kind,
                "conditions": conditions,
                "tolerations": tolerations,
                "effective_criticality": effective_criticality,
                "organization": organization,
                "workspace": workspace,
                "created": created,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "last_action_run": last_action_run,
                "block": block,
                "kubernetes_apps": kubernetes_apps,
                "product": product,
                "computed_cost": computed_cost,
                "cluster_domain": cluster_domain,
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
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if scope is not UNSET:
            field_dict["scope"] = scope
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
        if kubernetes_version is not UNSET:
            field_dict["kubernetes_version"] = kubernetes_version
        if installed is not UNSET:
            field_dict["installed"] = installed
        if is_host_cluster is not UNSET:
            field_dict["is_host_cluster"] = is_host_cluster
        if is_infrastructure_cluster is not UNSET:
            field_dict["is_infrastructure_cluster"] = is_infrastructure_cluster
        if kubeconfig_ca_cert_expiry_date is not UNSET:
            field_dict["kubeconfig_ca_cert_expiry_date"] = kubeconfig_ca_cert_expiry_date
        if kubeconfig_client_cert_expiry_date is not UNSET:
            field_dict["kubeconfig_client_cert_expiry_date"] = kubeconfig_client_cert_expiry_date
        if api_server_cert_expiry_date is not UNSET:
            field_dict["api_server_cert_expiry_date"] = api_server_cert_expiry_date
        if credential is not UNSET:
            field_dict["credential"] = credential
        if discovery_ignored_namespaces is not UNSET:
            field_dict["discovery_ignored_namespaces"] = discovery_ignored_namespaces
        if operator_loglevel is not UNSET:
            field_dict["operator_loglevel"] = operator_loglevel
        if operator_ignore_namespaces is not UNSET:
            field_dict["operator_ignore_namespaces"] = operator_ignore_namespaces
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if addons is not UNSET:
            field_dict["addons"] = addons
        if active is not UNSET:
            field_dict["active"] = active
        if backup_schedules is not UNSET:
            field_dict["backup_schedules"] = backup_schedules
        if baserow_id is not UNSET:
            field_dict["baserow_id"] = baserow_id
        if gitlab_project_id is not UNSET:
            field_dict["gitlab_project_id"] = gitlab_project_id
        if last_backup_import is not UNSET:
            field_dict["last_backup_import"] = last_backup_import
        if platform_dns_record_created is not UNSET:
            field_dict["platform_dns_record_created"] = platform_dns_record_created
        if slug is not UNSET:
            field_dict["slug"] = slug
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_simple import BlockSimple  # noqa: PLC0415
        from ..models.k8s_app_list import K8SAppList  # noqa: PLC0415
        from ..models.k8s_cluster_created import K8SClusterCreated  # noqa: PLC0415
        from ..models.k8s_cluster_deleted_by_user_type_0 import K8SClusterDeletedByUserType0  # noqa: PLC0415
        from ..models.k8s_cluster_last_action_run_type_0 import K8SClusterLastActionRunType0  # noqa: PLC0415
        from ..models.k8s_cluster_organization_type_0 import K8SClusterOrganizationType0  # noqa: PLC0415
        from ..models.k8s_cluster_workspace_type_0 import K8SClusterWorkspaceType0  # noqa: PLC0415
        from ..models.product_simple import ProductSimple  # noqa: PLC0415

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

        def _parse_deleted_by_user(data: object) -> K8SClusterDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = K8SClusterDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

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

        kind = check_k8s_cluster_kind_enum(d.pop("kind"))

        conditions = d.pop("conditions")

        tolerations = d.pop("tolerations")

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

        def _parse_organization(data: object) -> K8SClusterOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SClusterOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> K8SClusterWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SClusterWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SClusterCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> K8SClusterLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = K8SClusterLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        block = BlockSimple.from_dict(d.pop("block"))

        kubernetes_apps = []
        _kubernetes_apps = d.pop("kubernetes_apps")
        for kubernetes_apps_item_data in _kubernetes_apps:
            kubernetes_apps_item = K8SAppList.from_dict(kubernetes_apps_item_data)

            kubernetes_apps.append(kubernetes_apps_item)

        product = ProductSimple.from_dict(d.pop("product"))

        computed_cost = d.pop("computed_cost")

        def _parse_cluster_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cluster_domain = _parse_cluster_domain(d.pop("cluster_domain"))

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

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        platform_service = d.pop("platform_service", UNSET)

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

        def _parse_kubernetes_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubernetes_version = _parse_kubernetes_version(d.pop("kubernetes_version", UNSET))

        installed = d.pop("installed", UNSET)

        is_host_cluster = d.pop("is_host_cluster", UNSET)

        is_infrastructure_cluster = d.pop("is_infrastructure_cluster", UNSET)

        def _parse_kubeconfig_ca_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_ca_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_ca_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        kubeconfig_ca_cert_expiry_date = _parse_kubeconfig_ca_cert_expiry_date(
            d.pop("kubeconfig_ca_cert_expiry_date", UNSET)
        )

        def _parse_kubeconfig_client_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_client_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_client_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        kubeconfig_client_cert_expiry_date = _parse_kubeconfig_client_cert_expiry_date(
            d.pop("kubeconfig_client_cert_expiry_date", UNSET)
        )

        def _parse_api_server_cert_expiry_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                api_server_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return api_server_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        api_server_cert_expiry_date = _parse_api_server_cert_expiry_date(d.pop("api_server_cert_expiry_date", UNSET))

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        discovery_ignored_namespaces = d.pop("discovery_ignored_namespaces", UNSET)

        operator_loglevel = d.pop("operator_loglevel", UNSET)

        operator_ignore_namespaces = d.pop("operator_ignore_namespaces", UNSET)

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        addons = d.pop("addons", UNSET)

        active = d.pop("active", UNSET)

        backup_schedules = d.pop("backup_schedules", UNSET)

        def _parse_baserow_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        baserow_id = _parse_baserow_id(d.pop("baserow_id", UNSET))

        def _parse_gitlab_project_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gitlab_project_id = _parse_gitlab_project_id(d.pop("gitlab_project_id", UNSET))

        def _parse_last_backup_import(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_import_type_0 = datetime.datetime.fromisoformat(data)

                return last_backup_import_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_import = _parse_last_backup_import(d.pop("last_backup_import", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_managed_by_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        k8s_cluster = cls(
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
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            kind=kind,
            conditions=conditions,
            tolerations=tolerations,
            effective_criticality=effective_criticality,
            organization=organization,
            workspace=workspace,
            created=created,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            last_action_run=last_action_run,
            block=block,
            kubernetes_apps=kubernetes_apps,
            product=product,
            computed_cost=computed_cost,
            cluster_domain=cluster_domain,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            discovery_enabled=discovery_enabled,
            platform_service=platform_service,
            scope=scope,
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
            kubernetes_version=kubernetes_version,
            installed=installed,
            is_host_cluster=is_host_cluster,
            is_infrastructure_cluster=is_infrastructure_cluster,
            kubeconfig_ca_cert_expiry_date=kubeconfig_ca_cert_expiry_date,
            kubeconfig_client_cert_expiry_date=kubeconfig_client_cert_expiry_date,
            api_server_cert_expiry_date=api_server_cert_expiry_date,
            credential=credential,
            discovery_ignored_namespaces=discovery_ignored_namespaces,
            operator_loglevel=operator_loglevel,
            operator_ignore_namespaces=operator_ignore_namespaces,
            alias=alias,
            description=description,
            addons=addons,
            active=active,
            backup_schedules=backup_schedules,
            baserow_id=baserow_id,
            gitlab_project_id=gitlab_project_id,
            last_backup_import=last_backup_import,
            platform_dns_record_created=platform_dns_record_created,
            slug=slug,
            managed_by_content_type=managed_by_content_type,
            managed_by_object_id=managed_by_object_id,
        )

        k8s_cluster.additional_properties = d
        return k8s_cluster

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
