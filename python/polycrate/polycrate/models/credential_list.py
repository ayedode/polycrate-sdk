from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_kind_enum import CredentialKindEnum, check_credential_kind_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_list_active_condition_instances_item import CredentialListActiveConditionInstancesItem
    from ..models.credential_list_created import CredentialListCreated
    from ..models.credential_list_user_type_0 import CredentialListUserType0
    from ..models.organization_simple import OrganizationSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="CredentialList")


@_attrs_define
class CredentialList:
    """Lightweight serializer for Credential list views.

    Attributes:
        id (UUID):
        name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        labels (Any):
        conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
            conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
        condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
            Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
        active_condition_instances (list[CredentialListActiveConditionInstancesItem]):
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (WorkspaceSimple):
        created (CredentialListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (EffectiveCriticalityEnum | None):
        url (str): Gibt die absolute URL zum Object zurück.
        user (CredentialListUserType0 | None):
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
            * `provider-account` - Provider Account
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
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[CredentialListActiveConditionInstancesItem]
    organization: OrganizationSimple
    organization_priority: bool
    workspace: WorkspaceSimple
    created: CredentialListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    user: CredentialListUserType0 | None
    kind: CredentialKindEnum | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_list_user_type_0 import CredentialListUserType0

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization = self.organization.to_dict()

        organization_priority = self.organization_priority

        workspace = self.workspace.to_dict()

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        user: dict[str, Any] | None
        if isinstance(self.user, CredentialListUserType0):
            user = self.user.to_dict()
        else:
            user = self.user

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "user": user,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_list_active_condition_instances_item import CredentialListActiveConditionInstancesItem
        from ..models.credential_list_created import CredentialListCreated
        from ..models.credential_list_user_type_0 import CredentialListUserType0
        from ..models.organization_simple import OrganizationSimple
        from ..models.workspace_simple import WorkspaceSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = CredentialListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        created = CredentialListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

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

        url = d.pop("url")

        def _parse_user(data: object) -> CredentialListUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = CredentialListUserType0.from_dict(data)

                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialListUserType0 | None, data)

        user = _parse_user(d.pop("user"))

        _kind = d.pop("kind", UNSET)
        kind: CredentialKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_credential_kind_enum(_kind)

        _provider = d.pop("provider", UNSET)
        provider: ProviderEnum | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_enum(_provider)

        credential_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            user=user,
            kind=kind,
            provider=provider,
        )

        credential_list.additional_properties = d
        return credential_list

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
