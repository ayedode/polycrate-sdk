from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.loadbalancer_instance_criticality_type_1 import (
    LoadbalancerInstanceCriticalityType1,
    check_loadbalancer_instance_criticality_type_1,
)
from ..models.loadbalancer_instance_criticality_type_2_type_1 import (
    LoadbalancerInstanceCriticalityType2Type1,
    check_loadbalancer_instance_criticality_type_2_type_1,
)
from ..models.loadbalancer_instance_criticality_type_3_type_1 import (
    LoadbalancerInstanceCriticalityType3Type1,
    check_loadbalancer_instance_criticality_type_3_type_1,
)
from ..models.loadbalancer_instance_delegation_source_type_1 import (
    LoadbalancerInstanceDelegationSourceType1,
    check_loadbalancer_instance_delegation_source_type_1,
)
from ..models.loadbalancer_instance_delegation_source_type_2_type_1 import (
    LoadbalancerInstanceDelegationSourceType2Type1,
    check_loadbalancer_instance_delegation_source_type_2_type_1,
)
from ..models.loadbalancer_instance_delegation_source_type_3_type_1 import (
    LoadbalancerInstanceDelegationSourceType3Type1,
    check_loadbalancer_instance_delegation_source_type_3_type_1,
)
from ..models.loadbalancer_instance_deployment_strategy import (
    LoadbalancerInstanceDeploymentStrategy,
    check_loadbalancer_instance_deployment_strategy,
)
from ..models.loadbalancer_instance_effective_criticality_type_1 import (
    LoadbalancerInstanceEffectiveCriticalityType1,
    check_loadbalancer_instance_effective_criticality_type_1,
)
from ..models.loadbalancer_instance_effective_criticality_type_2_type_1 import (
    LoadbalancerInstanceEffectiveCriticalityType2Type1,
    check_loadbalancer_instance_effective_criticality_type_2_type_1,
)
from ..models.loadbalancer_instance_effective_criticality_type_3_type_1 import (
    LoadbalancerInstanceEffectiveCriticalityType3Type1,
    check_loadbalancer_instance_effective_criticality_type_3_type_1,
)
from ..models.loadbalancer_instance_engine_version import (
    LoadbalancerInstanceEngineVersion,
    check_loadbalancer_instance_engine_version,
)
from ..models.loadbalancer_instance_kind import LoadbalancerInstanceKind, check_loadbalancer_instance_kind
from ..models.loadbalancer_instance_last_state import (
    LoadbalancerInstanceLastState,
    check_loadbalancer_instance_last_state,
)
from ..models.loadbalancer_instance_protocol_mode import (
    LoadbalancerInstanceProtocolMode,
    check_loadbalancer_instance_protocol_mode,
)
from ..models.loadbalancer_instance_provider import LoadbalancerInstanceProvider, check_loadbalancer_instance_provider
from ..models.loadbalancer_instance_proxy_placement import (
    LoadbalancerInstanceProxyPlacement,
    check_loadbalancer_instance_proxy_placement,
)
from ..models.loadbalancer_instance_scope import LoadbalancerInstanceScope, check_loadbalancer_instance_scope
from ..models.loadbalancer_instance_session_affinity import (
    LoadbalancerInstanceSessionAffinity,
    check_loadbalancer_instance_session_affinity,
)
from ..models.loadbalancer_instance_state import LoadbalancerInstanceState, check_loadbalancer_instance_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_simple import CertificateSimple
    from ..models.ip_address_simple import IPAddressSimple
    from ..models.lbi_v2_spec import LbiV2Spec
    from ..models.loadbalancer_instance_created import LoadbalancerInstanceCreated
    from ..models.loadbalancer_instance_deleted_by_user_type_0 import LoadbalancerInstanceDeletedByUserType0
    from ..models.loadbalancer_instance_deployment import LoadbalancerInstanceDeployment
    from ..models.loadbalancer_instance_deployment_summary import LoadbalancerInstanceDeploymentSummary
    from ..models.loadbalancer_instance_effective_haproxy_defaults import LoadbalancerInstanceEffectiveHaproxyDefaults
    from ..models.loadbalancer_instance_effective_resources import LoadbalancerInstanceEffectiveResources
    from ..models.loadbalancer_instance_last_action_run_type_0 import LoadbalancerInstanceLastActionRunType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.product_simple import ProductSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="LoadbalancerInstance")


@_attrs_define
class LoadbalancerInstance:
    """Detail serializer for LoadbalancerInstance — erbt von ManagedObjectDetailSerializer.
    Spec: polycrate spec inspect 70

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            deleted_by_user (LoadbalancerInstanceDeletedByUserType0 | None):
            state (LoadbalancerInstanceState): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (LoadbalancerInstanceLastState): * `OK` - Ok
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
            scope (LoadbalancerInstanceScope): The scope is used to separate `system` owned objects from `user` owned
                objects.

                * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            tolerations (Any): Tolerations match conditions. If a toleration for a condition exists for an object, the
                condition will not be applied.
            effective_criticality (LoadbalancerInstanceEffectiveCriticalityType1 |
                LoadbalancerInstanceEffectiveCriticalityType2Type1 | LoadbalancerInstanceEffectiveCriticalityType3Type1 | None):
            actual_availability (str): Calculated actual availability as yearly average in %
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            workspace (WorkspaceSimple):
            created (LoadbalancerInstanceCreated):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            last_action_run (LoadbalancerInstanceLastActionRunType0 | None): Gibt den letzten ActionRun für das Objekt
                zurück (für Dashboard Footer).

                Unterstützte Relationen:
                - Direkter action_runs Manager (Workspace, Block, Organization)
                - Workspace-FK-Fallback, nur wenn show_last_action_run=True (K8sCluster, K8sApp)

                Spec: polycrate spec inspect 271
            region_deployments (list[LoadbalancerInstanceDeployment]):
            deployment_summary (LoadbalancerInstanceDeploymentSummary):
            deployments_ready (int):
            deployments_total (int):
            ip_address (IPAddressSimple): Simple serializer for IPAddress references in LoadBalancer context
            ip_address_value (None | str):
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            computed_cost (float):
            protocol_mode (LoadbalancerInstanceProtocolMode): * `tcp` - TCP
                * `http` - HTTP
            delegated_organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            delegated_workspace (WorkspaceSimple):
            loopback_resource_id (None | str): Loopback API entity id (e.g. load-balancer id).
            delegation_source (LoadbalancerInstanceDelegationSourceType1 | LoadbalancerInstanceDelegationSourceType2Type1 |
                LoadbalancerInstanceDelegationSourceType3Type1 | None): Source of the delegation mapping.

                * `loopback_lb` - Loopback Load Balancer
                * `loopback_object_store` - Loopback Object Store
            resource_limits (Any): Optional HAProxy limit overrides: {cpu, memory}. Empty inherits SystemConfig.
            effective_resources (LoadbalancerInstanceEffectiveResources):
            haproxy_defaults (Any): Optional HAProxy defaults overrides: {timeout_client_fin, timeout_server_fin,
                option_clitcpka, option_srvtcpka}. Empty inherits SystemConfig.
            effective_haproxy_defaults (LoadbalancerInstanceEffectiveHaproxyDefaults):
            issued_certificate (CertificateSimple): Simple serializer for embedding Certificate in other serializers.
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (LoadbalancerInstanceProvider | Unset): * `loopback` - Loopback
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
            kind (LoadbalancerInstanceKind | Unset): * `generic` - Generic
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (LoadbalancerInstanceCriticalityType1 | LoadbalancerInstanceCriticalityType2Type1 |
                LoadbalancerInstanceCriticalityType3Type1 | None | Unset): Criticality level. Null = inherit from workspace,
                then org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            ports (Any | Unset): Port configuration: [{port: 80, name: 'port-80', protocol: 'TCP', target_port: 80}]
            config (str | Unset): Load Balancer specific configuration (YAML/JSON)
            consumer_meta (Any | Unset): Arbitrary metadata from the consumer of this LoadBalancer instance
            enable_ssl (bool | Unset):
            ssl_redirect (bool | Unset):
            enable_websockets (bool | Unset):
            enable_grpc (bool | Unset):
            session_affinity (LoadbalancerInstanceSessionAffinity | Unset): * `none` - None
                * `cookie` - Cookie-based
                * `ip` - Client IP
            deployment_strategy (LoadbalancerInstanceDeploymentStrategy | Unset): * `rolling` - Rolling Update
                * `blue_green` - Blue-Green
                * `canary` - Canary
            last_deployment (datetime.datetime | None | Unset):
            metrics_data (Any | Unset): Metrics data from VictoriaMetrics: connections, bytes in/out with medians for 1h,
                24h, 30d
            engine_version (LoadbalancerInstanceEngineVersion | Unset): 1 = HAProxy BlockRollout, 2 = Envoy Gateway API SSA.
                Spec 705.

                * `1` - HAProxy (v1)
                * `2` - Envoy / Gateway API (v2)
            spec (LbiV2Spec | None | Unset):
            proxy_placement (LoadbalancerInstanceProxyPlacement | Unset): v2 placement. shared is rejected until a later
                spec.

                * `dedicated` - Dedicated
                * `shared` - Shared
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: LoadbalancerInstanceDeletedByUserType0 | None
    state: LoadbalancerInstanceState
    state_reason: None | str
    last_state: LoadbalancerInstanceLastState
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
    scope: LoadbalancerInstanceScope
    conditions: Any
    tolerations: Any
    effective_criticality: (
        LoadbalancerInstanceEffectiveCriticalityType1
        | LoadbalancerInstanceEffectiveCriticalityType2Type1
        | LoadbalancerInstanceEffectiveCriticalityType3Type1
        | None
    )
    actual_availability: str
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    created: LoadbalancerInstanceCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: LoadbalancerInstanceLastActionRunType0 | None
    region_deployments: list[LoadbalancerInstanceDeployment]
    deployment_summary: LoadbalancerInstanceDeploymentSummary
    deployments_ready: int
    deployments_total: int
    ip_address: IPAddressSimple
    ip_address_value: None | str
    product: ProductSimple
    computed_cost: float
    protocol_mode: LoadbalancerInstanceProtocolMode
    delegated_organization: OrganizationSimple
    delegated_workspace: WorkspaceSimple
    loopback_resource_id: None | str
    delegation_source: (
        LoadbalancerInstanceDelegationSourceType1
        | LoadbalancerInstanceDelegationSourceType2Type1
        | LoadbalancerInstanceDelegationSourceType3Type1
        | None
    )
    resource_limits: Any
    effective_resources: LoadbalancerInstanceEffectiveResources
    haproxy_defaults: Any
    effective_haproxy_defaults: LoadbalancerInstanceEffectiveHaproxyDefaults
    issued_certificate: CertificateSimple
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: LoadbalancerInstanceProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: LoadbalancerInstanceKind | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: (
        LoadbalancerInstanceCriticalityType1
        | LoadbalancerInstanceCriticalityType2Type1
        | LoadbalancerInstanceCriticalityType3Type1
        | None
        | Unset
    ) = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    ports: Any | Unset = UNSET
    config: str | Unset = UNSET
    consumer_meta: Any | Unset = UNSET
    enable_ssl: bool | Unset = UNSET
    ssl_redirect: bool | Unset = UNSET
    enable_websockets: bool | Unset = UNSET
    enable_grpc: bool | Unset = UNSET
    session_affinity: LoadbalancerInstanceSessionAffinity | Unset = UNSET
    deployment_strategy: LoadbalancerInstanceDeploymentStrategy | Unset = UNSET
    last_deployment: datetime.datetime | None | Unset = UNSET
    metrics_data: Any | Unset = UNSET
    engine_version: LoadbalancerInstanceEngineVersion | Unset = UNSET
    spec: LbiV2Spec | None | Unset = UNSET
    proxy_placement: LoadbalancerInstanceProxyPlacement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_spec import LbiV2Spec  # noqa: PLC0415
        from ..models.loadbalancer_instance_deleted_by_user_type_0 import LoadbalancerInstanceDeletedByUserType0  # noqa: PLC0415
        from ..models.loadbalancer_instance_last_action_run_type_0 import LoadbalancerInstanceLastActionRunType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, LoadbalancerInstanceDeletedByUserType0):
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

        tolerations = self.tolerations

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

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        created = self.created.to_dict()

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, LoadbalancerInstanceLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        region_deployments = []
        for region_deployments_item_data in self.region_deployments:
            region_deployments_item = region_deployments_item_data.to_dict()
            region_deployments.append(region_deployments_item)

        deployment_summary = self.deployment_summary.to_dict()

        deployments_ready = self.deployments_ready

        deployments_total = self.deployments_total

        ip_address = self.ip_address.to_dict()

        ip_address_value: None | str
        ip_address_value = self.ip_address_value

        product = self.product.to_dict()

        computed_cost = self.computed_cost

        protocol_mode: str = self.protocol_mode

        delegated_organization = self.delegated_organization.to_dict()

        delegated_workspace = self.delegated_workspace.to_dict()

        loopback_resource_id: None | str
        loopback_resource_id = self.loopback_resource_id

        delegation_source: None | str
        if isinstance(self.delegation_source, str):
            delegation_source = self.delegation_source
        elif isinstance(self.delegation_source, str):
            delegation_source = self.delegation_source
        elif isinstance(self.delegation_source, str):
            delegation_source = self.delegation_source
        else:
            delegation_source = self.delegation_source

        resource_limits = self.resource_limits

        effective_resources = self.effective_resources.to_dict()

        haproxy_defaults = self.haproxy_defaults

        effective_haproxy_defaults = self.effective_haproxy_defaults.to_dict()

        issued_certificate = self.issued_certificate.to_dict()

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

        ports = self.ports

        config = self.config

        consumer_meta = self.consumer_meta

        enable_ssl = self.enable_ssl

        ssl_redirect = self.ssl_redirect

        enable_websockets = self.enable_websockets

        enable_grpc = self.enable_grpc

        session_affinity: str | Unset = UNSET
        if not isinstance(self.session_affinity, Unset):
            session_affinity = self.session_affinity

        deployment_strategy: str | Unset = UNSET
        if not isinstance(self.deployment_strategy, Unset):
            deployment_strategy = self.deployment_strategy

        last_deployment: None | str | Unset
        if isinstance(self.last_deployment, Unset):
            last_deployment = UNSET
        elif isinstance(self.last_deployment, datetime.datetime):
            last_deployment = self.last_deployment.isoformat()
        else:
            last_deployment = self.last_deployment

        metrics_data = self.metrics_data

        engine_version: int | Unset = UNSET
        if not isinstance(self.engine_version, Unset):
            engine_version = self.engine_version

        spec: dict[str, Any] | None | Unset
        if isinstance(self.spec, Unset):
            spec = UNSET
        elif isinstance(self.spec, LbiV2Spec):
            spec = self.spec.to_dict()
        else:
            spec = self.spec

        proxy_placement: str | Unset = UNSET
        if not isinstance(self.proxy_placement, Unset):
            proxy_placement = self.proxy_placement

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
                "tolerations": tolerations,
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
                "region_deployments": region_deployments,
                "deployment_summary": deployment_summary,
                "deployments_ready": deployments_ready,
                "deployments_total": deployments_total,
                "ip_address": ip_address,
                "ip_address_value": ip_address_value,
                "product": product,
                "computed_cost": computed_cost,
                "protocol_mode": protocol_mode,
                "delegated_organization": delegated_organization,
                "delegated_workspace": delegated_workspace,
                "loopback_resource_id": loopback_resource_id,
                "delegation_source": delegation_source,
                "resource_limits": resource_limits,
                "effective_resources": effective_resources,
                "haproxy_defaults": haproxy_defaults,
                "effective_haproxy_defaults": effective_haproxy_defaults,
                "issued_certificate": issued_certificate,
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
        if ports is not UNSET:
            field_dict["ports"] = ports
        if config is not UNSET:
            field_dict["config"] = config
        if consumer_meta is not UNSET:
            field_dict["consumer_meta"] = consumer_meta
        if enable_ssl is not UNSET:
            field_dict["enable_ssl"] = enable_ssl
        if ssl_redirect is not UNSET:
            field_dict["ssl_redirect"] = ssl_redirect
        if enable_websockets is not UNSET:
            field_dict["enable_websockets"] = enable_websockets
        if enable_grpc is not UNSET:
            field_dict["enable_grpc"] = enable_grpc
        if session_affinity is not UNSET:
            field_dict["session_affinity"] = session_affinity
        if deployment_strategy is not UNSET:
            field_dict["deployment_strategy"] = deployment_strategy
        if last_deployment is not UNSET:
            field_dict["last_deployment"] = last_deployment
        if metrics_data is not UNSET:
            field_dict["metrics_data"] = metrics_data
        if engine_version is not UNSET:
            field_dict["engine_version"] = engine_version
        if spec is not UNSET:
            field_dict["spec"] = spec
        if proxy_placement is not UNSET:
            field_dict["proxy_placement"] = proxy_placement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_simple import CertificateSimple  # noqa: PLC0415
        from ..models.ip_address_simple import IPAddressSimple  # noqa: PLC0415
        from ..models.lbi_v2_spec import LbiV2Spec  # noqa: PLC0415
        from ..models.loadbalancer_instance_created import LoadbalancerInstanceCreated  # noqa: PLC0415
        from ..models.loadbalancer_instance_deleted_by_user_type_0 import LoadbalancerInstanceDeletedByUserType0  # noqa: PLC0415
        from ..models.loadbalancer_instance_deployment import LoadbalancerInstanceDeployment  # noqa: PLC0415
        from ..models.loadbalancer_instance_deployment_summary import LoadbalancerInstanceDeploymentSummary  # noqa: PLC0415
        from ..models.loadbalancer_instance_effective_haproxy_defaults import (
            LoadbalancerInstanceEffectiveHaproxyDefaults,  # noqa: PLC0415
        )
        from ..models.loadbalancer_instance_effective_resources import LoadbalancerInstanceEffectiveResources  # noqa: PLC0415
        from ..models.loadbalancer_instance_last_action_run_type_0 import LoadbalancerInstanceLastActionRunType0  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
        from ..models.product_simple import ProductSimple  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

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

        def _parse_deleted_by_user(data: object) -> LoadbalancerInstanceDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = LoadbalancerInstanceDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LoadbalancerInstanceDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        state = check_loadbalancer_instance_state(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_loadbalancer_instance_last_state(d.pop("last_state"))

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

        scope = check_loadbalancer_instance_scope(d.pop("scope"))

        conditions = d.pop("conditions")

        tolerations = d.pop("tolerations")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            LoadbalancerInstanceEffectiveCriticalityType1
            | LoadbalancerInstanceEffectiveCriticalityType2Type1
            | LoadbalancerInstanceEffectiveCriticalityType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_loadbalancer_instance_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_loadbalancer_instance_effective_criticality_type_2_type_1(
                    data
                )

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_loadbalancer_instance_effective_criticality_type_3_type_1(
                    data
                )

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LoadbalancerInstanceEffectiveCriticalityType1
                | LoadbalancerInstanceEffectiveCriticalityType2Type1
                | LoadbalancerInstanceEffectiveCriticalityType3Type1
                | None,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        actual_availability = d.pop("actual_availability")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = LoadbalancerInstanceCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> LoadbalancerInstanceLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = LoadbalancerInstanceLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LoadbalancerInstanceLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        region_deployments = []
        _region_deployments = d.pop("region_deployments")
        for region_deployments_item_data in _region_deployments:
            region_deployments_item = LoadbalancerInstanceDeployment.from_dict(region_deployments_item_data)

            region_deployments.append(region_deployments_item)

        deployment_summary = LoadbalancerInstanceDeploymentSummary.from_dict(d.pop("deployment_summary"))

        deployments_ready = d.pop("deployments_ready")

        deployments_total = d.pop("deployments_total")

        ip_address = IPAddressSimple.from_dict(d.pop("ip_address"))

        def _parse_ip_address_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address_value = _parse_ip_address_value(d.pop("ip_address_value"))

        product = ProductSimple.from_dict(d.pop("product"))

        computed_cost = d.pop("computed_cost")

        protocol_mode = check_loadbalancer_instance_protocol_mode(d.pop("protocol_mode"))

        delegated_organization = OrganizationSimple.from_dict(d.pop("delegated_organization"))

        delegated_workspace = WorkspaceSimple.from_dict(d.pop("delegated_workspace"))

        def _parse_loopback_resource_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        loopback_resource_id = _parse_loopback_resource_id(d.pop("loopback_resource_id"))

        def _parse_delegation_source(
            data: object,
        ) -> (
            LoadbalancerInstanceDelegationSourceType1
            | LoadbalancerInstanceDelegationSourceType2Type1
            | LoadbalancerInstanceDelegationSourceType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegation_source_type_1 = check_loadbalancer_instance_delegation_source_type_1(data)

                return delegation_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegation_source_type_2_type_1 = check_loadbalancer_instance_delegation_source_type_2_type_1(data)

                return delegation_source_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegation_source_type_3_type_1 = check_loadbalancer_instance_delegation_source_type_3_type_1(data)

                return delegation_source_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LoadbalancerInstanceDelegationSourceType1
                | LoadbalancerInstanceDelegationSourceType2Type1
                | LoadbalancerInstanceDelegationSourceType3Type1
                | None,
                data,
            )

        delegation_source = _parse_delegation_source(d.pop("delegation_source"))

        resource_limits = d.pop("resource_limits")

        effective_resources = LoadbalancerInstanceEffectiveResources.from_dict(d.pop("effective_resources"))

        haproxy_defaults = d.pop("haproxy_defaults")

        effective_haproxy_defaults = LoadbalancerInstanceEffectiveHaproxyDefaults.from_dict(
            d.pop("effective_haproxy_defaults")
        )

        issued_certificate = CertificateSimple.from_dict(d.pop("issued_certificate"))

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
        provider: LoadbalancerInstanceProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_loadbalancer_instance_provider(_provider)

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
        kind: LoadbalancerInstanceKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_loadbalancer_instance_kind(_kind)

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
            LoadbalancerInstanceCriticalityType1
            | LoadbalancerInstanceCriticalityType2Type1
            | LoadbalancerInstanceCriticalityType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_loadbalancer_instance_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_loadbalancer_instance_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_loadbalancer_instance_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                LoadbalancerInstanceCriticalityType1
                | LoadbalancerInstanceCriticalityType2Type1
                | LoadbalancerInstanceCriticalityType3Type1
                | None
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

        ports = d.pop("ports", UNSET)

        config = d.pop("config", UNSET)

        consumer_meta = d.pop("consumer_meta", UNSET)

        enable_ssl = d.pop("enable_ssl", UNSET)

        ssl_redirect = d.pop("ssl_redirect", UNSET)

        enable_websockets = d.pop("enable_websockets", UNSET)

        enable_grpc = d.pop("enable_grpc", UNSET)

        _session_affinity = d.pop("session_affinity", UNSET)
        session_affinity: LoadbalancerInstanceSessionAffinity | Unset
        if isinstance(_session_affinity, Unset):
            session_affinity = UNSET
        else:
            session_affinity = check_loadbalancer_instance_session_affinity(_session_affinity)

        _deployment_strategy = d.pop("deployment_strategy", UNSET)
        deployment_strategy: LoadbalancerInstanceDeploymentStrategy | Unset
        if isinstance(_deployment_strategy, Unset):
            deployment_strategy = UNSET
        else:
            deployment_strategy = check_loadbalancer_instance_deployment_strategy(_deployment_strategy)

        def _parse_last_deployment(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_deployment_type_0 = datetime.datetime.fromisoformat(data)

                return last_deployment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_deployment = _parse_last_deployment(d.pop("last_deployment", UNSET))

        metrics_data = d.pop("metrics_data", UNSET)

        _engine_version = d.pop("engine_version", UNSET)
        engine_version: LoadbalancerInstanceEngineVersion | Unset
        if isinstance(_engine_version, Unset):
            engine_version = UNSET
        else:
            engine_version = check_loadbalancer_instance_engine_version(_engine_version)

        def _parse_spec(data: object) -> LbiV2Spec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spec_type_1 = LbiV2Spec.from_dict(data)

                return spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2Spec | None | Unset, data)

        spec = _parse_spec(d.pop("spec", UNSET))

        _proxy_placement = d.pop("proxy_placement", UNSET)
        proxy_placement: LoadbalancerInstanceProxyPlacement | Unset
        if isinstance(_proxy_placement, Unset):
            proxy_placement = UNSET
        else:
            proxy_placement = check_loadbalancer_instance_proxy_placement(_proxy_placement)

        loadbalancer_instance = cls(
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
            tolerations=tolerations,
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
            region_deployments=region_deployments,
            deployment_summary=deployment_summary,
            deployments_ready=deployments_ready,
            deployments_total=deployments_total,
            ip_address=ip_address,
            ip_address_value=ip_address_value,
            product=product,
            computed_cost=computed_cost,
            protocol_mode=protocol_mode,
            delegated_organization=delegated_organization,
            delegated_workspace=delegated_workspace,
            loopback_resource_id=loopback_resource_id,
            delegation_source=delegation_source,
            resource_limits=resource_limits,
            effective_resources=effective_resources,
            haproxy_defaults=haproxy_defaults,
            effective_haproxy_defaults=effective_haproxy_defaults,
            issued_certificate=issued_certificate,
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
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            ports=ports,
            config=config,
            consumer_meta=consumer_meta,
            enable_ssl=enable_ssl,
            ssl_redirect=ssl_redirect,
            enable_websockets=enable_websockets,
            enable_grpc=enable_grpc,
            session_affinity=session_affinity,
            deployment_strategy=deployment_strategy,
            last_deployment=last_deployment,
            metrics_data=metrics_data,
            engine_version=engine_version,
            spec=spec,
            proxy_placement=proxy_placement,
        )

        loadbalancer_instance.additional_properties = d
        return loadbalancer_instance

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
