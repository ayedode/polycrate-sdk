from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.phase_enum import PhaseEnum, check_phase_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.reclaim_policy_enum import ReclaimPolicyEnum, check_reclaim_policy_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..models.volume_mode_enum import VolumeModeEnum, check_volume_mode_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="K8SVolumeRequest")


@_attrs_define
class K8SVolumeRequest:
    """K8sVolume Detail Serializer — used by the operator and API clients.
    Spec: polycrate spec inspect 31
    Pricing: polycrate spec inspect 155

    k8s_cluster and k8s_app are intentionally NOT declared as nested serializers here
    so that DRF auto-generates them as writable PrimaryKeyRelatedField (UUID).
    The operator must be able to set k8s_cluster on create/update.
    organization and workspace are handled by ManagedObjectBaseViewset.perform_create.

        Attributes:
            k8s_cluster (UUID):
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
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
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
            k8s_app (None | Unset | UUID): Matched via pvc_namespace against K8sApp.namespace
            provider_object_name (None | str | Unset):
            provider_object_id (None | str | Unset):
            cloud_provider_volume_id (None | str | Unset): Cloud provider volume identifier (e.g. Hetzner volume id),
                distinct from PV UID
            csi_driver (None | str | Unset): CSI driver name from PV.spec.csi.driver; null for non-CSI volumes
                (hostPath/local/nfs/…)
            storage_class (None | str | Unset):
            capacity_bytes (int | None | Unset):
            capacity_string (None | str | Unset): Original k8s Quantity string e.g. '10Gi', '500Mi'
            phase (PhaseEnum | Unset): * `Bound` - Bound
                * `Released` - Released
                * `Available` - Available
                * `Failed` - Failed
                * `Pending` - Pending
                * `Unknown` - Unknown
            access_modes (Any | Unset):
            volume_mode (VolumeModeEnum | Unset): * `Filesystem` - Filesystem
                * `Block` - Block
            reclaim_policy (ReclaimPolicyEnum | Unset): * `Retain` - Retain
                * `Delete` - Delete
                * `Recycle` - Recycle
            pvc_name (None | str | Unset):
            pvc_namespace (None | str | Unset):
            node_affinity (Any | Unset):
            managed_by_content_type (int | None | Unset):
            managed_by_object_id (None | str | Unset):
    """

    k8s_cluster: UUID
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
    kind: GenericObjectKindEnum | Unset = UNSET
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
    k8s_app: None | Unset | UUID = UNSET
    provider_object_name: None | str | Unset = UNSET
    provider_object_id: None | str | Unset = UNSET
    cloud_provider_volume_id: None | str | Unset = UNSET
    csi_driver: None | str | Unset = UNSET
    storage_class: None | str | Unset = UNSET
    capacity_bytes: int | None | Unset = UNSET
    capacity_string: None | str | Unset = UNSET
    phase: PhaseEnum | Unset = UNSET
    access_modes: Any | Unset = UNSET
    volume_mode: VolumeModeEnum | Unset = UNSET
    reclaim_policy: ReclaimPolicyEnum | Unset = UNSET
    pvc_name: None | str | Unset = UNSET
    pvc_namespace: None | str | Unset = UNSET
    node_affinity: Any | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        k8s_cluster = str(self.k8s_cluster)

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

        k8s_app: None | str | Unset
        if isinstance(self.k8s_app, Unset):
            k8s_app = UNSET
        elif isinstance(self.k8s_app, UUID):
            k8s_app = str(self.k8s_app)
        else:
            k8s_app = self.k8s_app

        provider_object_name: None | str | Unset
        if isinstance(self.provider_object_name, Unset):
            provider_object_name = UNSET
        else:
            provider_object_name = self.provider_object_name

        provider_object_id: None | str | Unset
        if isinstance(self.provider_object_id, Unset):
            provider_object_id = UNSET
        else:
            provider_object_id = self.provider_object_id

        cloud_provider_volume_id: None | str | Unset
        if isinstance(self.cloud_provider_volume_id, Unset):
            cloud_provider_volume_id = UNSET
        else:
            cloud_provider_volume_id = self.cloud_provider_volume_id

        csi_driver: None | str | Unset
        if isinstance(self.csi_driver, Unset):
            csi_driver = UNSET
        else:
            csi_driver = self.csi_driver

        storage_class: None | str | Unset
        if isinstance(self.storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = self.storage_class

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        capacity_string: None | str | Unset
        if isinstance(self.capacity_string, Unset):
            capacity_string = UNSET
        else:
            capacity_string = self.capacity_string

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase

        access_modes = self.access_modes

        volume_mode: str | Unset = UNSET
        if not isinstance(self.volume_mode, Unset):
            volume_mode = self.volume_mode

        reclaim_policy: str | Unset = UNSET
        if not isinstance(self.reclaim_policy, Unset):
            reclaim_policy = self.reclaim_policy

        pvc_name: None | str | Unset
        if isinstance(self.pvc_name, Unset):
            pvc_name = UNSET
        else:
            pvc_name = self.pvc_name

        pvc_namespace: None | str | Unset
        if isinstance(self.pvc_namespace, Unset):
            pvc_namespace = UNSET
        else:
            pvc_namespace = self.pvc_namespace

        node_affinity = self.node_affinity

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
                "k8s_cluster": k8s_cluster,
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
        if k8s_app is not UNSET:
            field_dict["k8s_app"] = k8s_app
        if provider_object_name is not UNSET:
            field_dict["provider_object_name"] = provider_object_name
        if provider_object_id is not UNSET:
            field_dict["provider_object_id"] = provider_object_id
        if cloud_provider_volume_id is not UNSET:
            field_dict["cloud_provider_volume_id"] = cloud_provider_volume_id
        if csi_driver is not UNSET:
            field_dict["csi_driver"] = csi_driver
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if capacity_bytes is not UNSET:
            field_dict["capacity_bytes"] = capacity_bytes
        if capacity_string is not UNSET:
            field_dict["capacity_string"] = capacity_string
        if phase is not UNSET:
            field_dict["phase"] = phase
        if access_modes is not UNSET:
            field_dict["access_modes"] = access_modes
        if volume_mode is not UNSET:
            field_dict["volume_mode"] = volume_mode
        if reclaim_policy is not UNSET:
            field_dict["reclaim_policy"] = reclaim_policy
        if pvc_name is not UNSET:
            field_dict["pvc_name"] = pvc_name
        if pvc_namespace is not UNSET:
            field_dict["pvc_namespace"] = pvc_namespace
        if node_affinity is not UNSET:
            field_dict["node_affinity"] = node_affinity
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("k8s_cluster", (None, str(self.k8s_cluster), "text/plain")))

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

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("discovery_enabled", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.k8s_app, Unset):
            if isinstance(self.k8s_app, UUID):
                files.append(("k8s_app", (None, str(self.k8s_app), "text/plain")))
            else:
                files.append(("k8s_app", (None, str(self.k8s_app).encode(), "text/plain")))

        if not isinstance(self.provider_object_name, Unset):
            if isinstance(self.provider_object_name, str):
                files.append(("provider_object_name", (None, str(self.provider_object_name).encode(), "text/plain")))
            else:
                files.append(("provider_object_name", (None, str(self.provider_object_name).encode(), "text/plain")))

        if not isinstance(self.provider_object_id, Unset):
            if isinstance(self.provider_object_id, str):
                files.append(("provider_object_id", (None, str(self.provider_object_id).encode(), "text/plain")))
            else:
                files.append(("provider_object_id", (None, str(self.provider_object_id).encode(), "text/plain")))

        if not isinstance(self.cloud_provider_volume_id, Unset):
            if isinstance(self.cloud_provider_volume_id, str):
                files.append(
                    ("cloud_provider_volume_id", (None, str(self.cloud_provider_volume_id).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("cloud_provider_volume_id", (None, str(self.cloud_provider_volume_id).encode(), "text/plain"))
                )

        if not isinstance(self.csi_driver, Unset):
            if isinstance(self.csi_driver, str):
                files.append(("csi_driver", (None, str(self.csi_driver).encode(), "text/plain")))
            else:
                files.append(("csi_driver", (None, str(self.csi_driver).encode(), "text/plain")))

        if not isinstance(self.storage_class, Unset):
            if isinstance(self.storage_class, str):
                files.append(("storage_class", (None, str(self.storage_class).encode(), "text/plain")))
            else:
                files.append(("storage_class", (None, str(self.storage_class).encode(), "text/plain")))

        if not isinstance(self.capacity_bytes, Unset):
            if isinstance(self.capacity_bytes, int):
                files.append(("capacity_bytes", (None, str(self.capacity_bytes).encode(), "text/plain")))
            else:
                files.append(("capacity_bytes", (None, str(self.capacity_bytes).encode(), "text/plain")))

        if not isinstance(self.capacity_string, Unset):
            if isinstance(self.capacity_string, str):
                files.append(("capacity_string", (None, str(self.capacity_string).encode(), "text/plain")))
            else:
                files.append(("capacity_string", (None, str(self.capacity_string).encode(), "text/plain")))

        if not isinstance(self.phase, Unset):
            files.append(("phase", (None, str(self.phase).encode(), "text/plain")))

        if not isinstance(self.access_modes, Unset):
            files.append(("access_modes", (None, str(self.access_modes).encode(), "text/plain")))

        if not isinstance(self.volume_mode, Unset):
            files.append(("volume_mode", (None, str(self.volume_mode).encode(), "text/plain")))

        if not isinstance(self.reclaim_policy, Unset):
            files.append(("reclaim_policy", (None, str(self.reclaim_policy).encode(), "text/plain")))

        if not isinstance(self.pvc_name, Unset):
            if isinstance(self.pvc_name, str):
                files.append(("pvc_name", (None, str(self.pvc_name).encode(), "text/plain")))
            else:
                files.append(("pvc_name", (None, str(self.pvc_name).encode(), "text/plain")))

        if not isinstance(self.pvc_namespace, Unset):
            if isinstance(self.pvc_namespace, str):
                files.append(("pvc_namespace", (None, str(self.pvc_namespace).encode(), "text/plain")))
            else:
                files.append(("pvc_namespace", (None, str(self.pvc_namespace).encode(), "text/plain")))

        if not isinstance(self.node_affinity, Unset):
            files.append(("node_affinity", (None, str(self.node_affinity).encode(), "text/plain")))

        if not isinstance(self.managed_by_content_type, Unset):
            if isinstance(self.managed_by_content_type, int):
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )

        if not isinstance(self.managed_by_object_id, Unset):
            if isinstance(self.managed_by_object_id, str):
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))
            else:
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        k8s_cluster = UUID(d.pop("k8s_cluster"))

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

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

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

        def _parse_k8s_app(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_app_type_0 = UUID(data)

                return k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        k8s_app = _parse_k8s_app(d.pop("k8s_app", UNSET))

        def _parse_provider_object_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_object_name = _parse_provider_object_name(d.pop("provider_object_name", UNSET))

        def _parse_provider_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_object_id = _parse_provider_object_id(d.pop("provider_object_id", UNSET))

        def _parse_cloud_provider_volume_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_provider_volume_id = _parse_cloud_provider_volume_id(d.pop("cloud_provider_volume_id", UNSET))

        def _parse_csi_driver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csi_driver = _parse_csi_driver(d.pop("csi_driver", UNSET))

        def _parse_storage_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_class = _parse_storage_class(d.pop("storage_class", UNSET))

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacity_bytes", UNSET))

        def _parse_capacity_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_string = _parse_capacity_string(d.pop("capacity_string", UNSET))

        _phase = d.pop("phase", UNSET)
        phase: PhaseEnum | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = check_phase_enum(_phase)

        access_modes = d.pop("access_modes", UNSET)

        _volume_mode = d.pop("volume_mode", UNSET)
        volume_mode: VolumeModeEnum | Unset
        if isinstance(_volume_mode, Unset):
            volume_mode = UNSET
        else:
            volume_mode = check_volume_mode_enum(_volume_mode)

        _reclaim_policy = d.pop("reclaim_policy", UNSET)
        reclaim_policy: ReclaimPolicyEnum | Unset
        if isinstance(_reclaim_policy, Unset):
            reclaim_policy = UNSET
        else:
            reclaim_policy = check_reclaim_policy_enum(_reclaim_policy)

        def _parse_pvc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pvc_name = _parse_pvc_name(d.pop("pvc_name", UNSET))

        def _parse_pvc_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pvc_namespace = _parse_pvc_namespace(d.pop("pvc_namespace", UNSET))

        node_affinity = d.pop("node_affinity", UNSET)

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

        k8s_volume_request = cls(
            k8s_cluster=k8s_cluster,
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
            kind=kind,
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
            k8s_app=k8s_app,
            provider_object_name=provider_object_name,
            provider_object_id=provider_object_id,
            cloud_provider_volume_id=cloud_provider_volume_id,
            csi_driver=csi_driver,
            storage_class=storage_class,
            capacity_bytes=capacity_bytes,
            capacity_string=capacity_string,
            phase=phase,
            access_modes=access_modes,
            volume_mode=volume_mode,
            reclaim_policy=reclaim_policy,
            pvc_name=pvc_name,
            pvc_namespace=pvc_namespace,
            node_affinity=node_affinity,
            managed_by_content_type=managed_by_content_type,
            managed_by_object_id=managed_by_object_id,
        )

        k8s_volume_request.additional_properties = d
        return k8s_volume_request

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
