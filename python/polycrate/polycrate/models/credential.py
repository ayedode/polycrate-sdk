from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_created import CredentialCreated
    from ..models.credential_deleted_by_user_type_0 import CredentialDeletedByUserType0
    from ..models.credential_last_action_run_type_0 import CredentialLastActionRunType0
    from ..models.credential_secrets_type_0 import CredentialSecretsType0
    from ..models.credential_user_type_0 import CredentialUserType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="Credential")


@_attrs_define
class Credential:
    """Full serializer for Credential detail views.

    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
        is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
            runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
        deleted_by_user (CredentialDeletedByUserType0 | None):
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
        effective_criticality (EffectiveCriticalityEnum | None):
        actual_availability (str): Calculated actual availability as yearly average in %
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (WorkspaceSimple):
        created (CredentialCreated):
        url (str): Gibt die absolute URL zum Object zurück.
        icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
            Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
        is_class_icon (bool):
        effective_slo_target (float | None): Gibt den effektiven SLO-Zielwert inkl. System-Default zurück.
            Spec: polycrate spec inspect 271
        effective_sla_target (float | None): Gibt den effektiven SLA-Zielwert inkl. System-Default zurück.
            Spec: polycrate spec inspect 271
        last_action_run (CredentialLastActionRunType0 | None): Gibt den letzten ActionRun für das Objekt zurück (für
            Dashboard Footer).

            Unterstützte Relationen:
            - Direkter action_runs Manager (Workspace, Block, Organization)
            - Workspace-FK-Fallback, nur wenn show_last_action_run=True (K8sCluster, K8sApp)

            Spec: polycrate spec inspect 271
        user (CredentialUserType0 | None):
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
        platform_service (bool | Unset):
        kind (CredentialKindEnum | Unset): * `api-key` - API Key
            * `kubeconfig` - Kubeconfig
            * `s3-credential` - S3 Credential
            * `ssh-keys` - SSH Keys
            * `generic` - Generic
            * `webhook` - Webhook
            * `agent_token` - Agent Token
            * `workspace-encryption` - Workspace Encryption
            * `oci-registry-credential` - OCI Registry Credential
            * `helm-repository-credential` - Helm Repository Credential
            * `apmstack-metrics-credential` - APM Stack Metrics Credential
            * `unified-apm-credential` - Unified APM Credential
            * `unified-registry-credential` - Unified Registry Credential
            * `apmstack-logs-credential` - APM Stack Logs Credential
            * `apmstack-traces-credential` - APM Stack Traces Credential
            * `domain-auth-code` - Domain Auth Code
            * `dns-provider` - DNS Provider
            * `system_api_key` - System API Key
            * `org_api_key` - Org API Key
            * `controlplane-token` - Controlplane Token
            * `provider-account` - Provider Account Default: 'generic'.
        tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
            the condition will not be applied.
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
        slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
        slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
        sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
        sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
        api_endpoint (None | str | Unset):
        api_user (None | str | Unset):
        api_key (None | str | Unset):
        secrets (CredentialSecretsType0 | None | Unset): Credential secrets as JSON object (encrypted in database)
        kubeconfig (None | str | Unset):
        ssh_private_key (None | str | Unset):
        ssh_public_key (None | str | Unset):
        description (None | str | Unset):
        metadata (Any | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    deleted_by_user: CredentialDeletedByUserType0 | None
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
    effective_criticality: EffectiveCriticalityEnum | None
    actual_availability: str
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    created: CredentialCreated
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    last_action_run: CredentialLastActionRunType0 | None
    user: CredentialUserType0 | None
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: CredentialKindEnum | Unset = "generic"
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    api_endpoint: None | str | Unset = UNSET
    api_user: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    secrets: CredentialSecretsType0 | None | Unset = UNSET
    kubeconfig: None | str | Unset = UNSET
    ssh_private_key: None | str | Unset = UNSET
    ssh_public_key: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_deleted_by_user_type_0 import CredentialDeletedByUserType0  # noqa: PLC0415
        from ..models.credential_last_action_run_type_0 import CredentialLastActionRunType0  # noqa: PLC0415
        from ..models.credential_secrets_type_0 import CredentialSecretsType0  # noqa: PLC0415
        from ..models.credential_user_type_0 import CredentialUserType0  # noqa: PLC0415

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
        if isinstance(self.deleted_by_user, CredentialDeletedByUserType0):
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
        if isinstance(self.last_action_run, CredentialLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        user: dict[str, Any] | None
        if isinstance(self.user, CredentialUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

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

        api_endpoint: None | str | Unset
        if isinstance(self.api_endpoint, Unset):
            api_endpoint = UNSET
        else:
            api_endpoint = self.api_endpoint

        api_user: None | str | Unset
        if isinstance(self.api_user, Unset):
            api_user = UNSET
        else:
            api_user = self.api_user

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, CredentialSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        kubeconfig: None | str | Unset
        if isinstance(self.kubeconfig, Unset):
            kubeconfig = UNSET
        else:
            kubeconfig = self.kubeconfig

        ssh_private_key: None | str | Unset
        if isinstance(self.ssh_private_key, Unset):
            ssh_private_key = UNSET
        else:
            ssh_private_key = self.ssh_private_key

        ssh_public_key: None | str | Unset
        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        else:
            ssh_public_key = self.ssh_public_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata = self.metadata

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
                "user": user,
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
        if api_endpoint is not UNSET:
            field_dict["api_endpoint"] = api_endpoint
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if kubeconfig is not UNSET:
            field_dict["kubeconfig"] = kubeconfig
        if ssh_private_key is not UNSET:
            field_dict["ssh_private_key"] = ssh_private_key
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_created import CredentialCreated  # noqa: PLC0415
        from ..models.credential_deleted_by_user_type_0 import CredentialDeletedByUserType0  # noqa: PLC0415
        from ..models.credential_last_action_run_type_0 import CredentialLastActionRunType0  # noqa: PLC0415
        from ..models.credential_secrets_type_0 import CredentialSecretsType0  # noqa: PLC0415
        from ..models.credential_user_type_0 import CredentialUserType0  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
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

        def _parse_deleted_by_user(data: object) -> CredentialDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = CredentialDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialDeletedByUserType0 | None, data)

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

        actual_availability = d.pop("actual_availability")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = CredentialCreated.from_dict(d.pop("created"))

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

        def _parse_last_action_run(data: object) -> CredentialLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = CredentialLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_user(data: object) -> CredentialUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = CredentialUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialUserType0 | None, data)

        user = _parse_user(d.pop("user"))

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

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: CredentialKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_credential_kind_enum(_kind)

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

        def _parse_api_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_endpoint = _parse_api_endpoint(d.pop("api_endpoint", UNSET))

        def _parse_api_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_user = _parse_api_user(d.pop("api_user", UNSET))

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_secrets(data: object) -> CredentialSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = CredentialSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        def _parse_kubeconfig(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubeconfig = _parse_kubeconfig(d.pop("kubeconfig", UNSET))

        def _parse_ssh_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_private_key = _parse_ssh_private_key(d.pop("ssh_private_key", UNSET))

        def _parse_ssh_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_public_key = _parse_ssh_public_key(d.pop("ssh_public_key", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        metadata = d.pop("metadata", UNSET)

        credential = cls(
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
            user=user,
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
            api_endpoint=api_endpoint,
            api_user=api_user,
            api_key=api_key,
            secrets=secrets,
            kubeconfig=kubeconfig,
            ssh_private_key=ssh_private_key,
            ssh_public_key=ssh_public_key,
            description=description,
            metadata=metadata,
        )

        credential.additional_properties = d
        return credential

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
