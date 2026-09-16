from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.k8s_cluster_kind_enum import K8SClusterKindEnum, check_k8s_cluster_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.k8s_cluster_list_active_condition_instances_item import K8SClusterListActiveConditionInstancesItem
    from ..models.k8s_cluster_list_created import K8SClusterListCreated
    from ..models.k8s_cluster_list_organization_type_0 import K8SClusterListOrganizationType0
    from ..models.k8s_cluster_list_workspace_type_0 import K8SClusterListWorkspaceType0


T = TypeVar("T", bound="K8SClusterList")


@_attrs_define
class K8SClusterList:
    """K8sCluster List Serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created, reconciliation_running, url

    K8sCluster-spezifische Felder:
    - kind, kubernetes_version, conditions, etc.
    - slo_availability, sla_availability (Spec: .specs/0.11.24/sre-sla-slo-sli-framework.md)

    Per .specs/0.11.4/dynamic-table-v2.md

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
            active_condition_instances (list[K8SClusterListActiveConditionInstancesItem]):
            organization (K8SClusterListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (K8SClusterListWorkspaceType0 | None):
            created (K8SClusterListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            kind (K8SClusterKindEnum): * `polycrate` - Polycrate
                * `generic` - Generic
                * `loopback` - Loopback
            installed (bool):
            is_host_cluster (bool):
            is_infrastructure_cluster (bool):
            kubernetes_version (None | str):
            kubeconfig_ca_cert_expiry_date (datetime.datetime | None):
            kubeconfig_client_cert_expiry_date (datetime.datetime | None):
            api_server_cert_expiry_date (datetime.datetime | None):
            credential (None | UUID):
            slo_availability (str):
            sla_availability (str):
            slo_status (str):
            sla_status (str):
            has_active_downtime (bool):
            cluster_domain (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[K8SClusterListActiveConditionInstancesItem]
    organization: K8SClusterListOrganizationType0 | None
    organization_priority: bool
    workspace: K8SClusterListWorkspaceType0 | None
    created: K8SClusterListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    kind: K8SClusterKindEnum
    installed: bool
    is_host_cluster: bool
    is_infrastructure_cluster: bool
    kubernetes_version: None | str
    kubeconfig_ca_cert_expiry_date: datetime.datetime | None
    kubeconfig_client_cert_expiry_date: datetime.datetime | None
    api_server_cert_expiry_date: datetime.datetime | None
    credential: None | UUID
    slo_availability: str
    sla_availability: str
    slo_status: str
    sla_status: str
    has_active_downtime: bool
    cluster_domain: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.k8s_cluster_list_organization_type_0 import K8SClusterListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_cluster_list_workspace_type_0 import K8SClusterListWorkspaceType0  # noqa: PLC0415

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

        organization: dict[str, Any] | None
        if isinstance(self.organization, K8SClusterListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, K8SClusterListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        kind: str = self.kind

        installed = self.installed

        is_host_cluster = self.is_host_cluster

        is_infrastructure_cluster = self.is_infrastructure_cluster

        kubernetes_version: None | str
        kubernetes_version = self.kubernetes_version

        kubeconfig_ca_cert_expiry_date: None | str
        if isinstance(self.kubeconfig_ca_cert_expiry_date, datetime.datetime):
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date.isoformat()
        else:
            kubeconfig_ca_cert_expiry_date = self.kubeconfig_ca_cert_expiry_date

        kubeconfig_client_cert_expiry_date: None | str
        if isinstance(self.kubeconfig_client_cert_expiry_date, datetime.datetime):
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date.isoformat()
        else:
            kubeconfig_client_cert_expiry_date = self.kubeconfig_client_cert_expiry_date

        api_server_cert_expiry_date: None | str
        if isinstance(self.api_server_cert_expiry_date, datetime.datetime):
            api_server_cert_expiry_date = self.api_server_cert_expiry_date.isoformat()
        else:
            api_server_cert_expiry_date = self.api_server_cert_expiry_date

        credential: None | str
        if isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        slo_availability = self.slo_availability

        sla_availability = self.sla_availability

        slo_status = self.slo_status

        sla_status = self.sla_status

        has_active_downtime = self.has_active_downtime

        cluster_domain: None | str
        cluster_domain = self.cluster_domain

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
                "kind": kind,
                "installed": installed,
                "is_host_cluster": is_host_cluster,
                "is_infrastructure_cluster": is_infrastructure_cluster,
                "kubernetes_version": kubernetes_version,
                "kubeconfig_ca_cert_expiry_date": kubeconfig_ca_cert_expiry_date,
                "kubeconfig_client_cert_expiry_date": kubeconfig_client_cert_expiry_date,
                "api_server_cert_expiry_date": api_server_cert_expiry_date,
                "credential": credential,
                "slo_availability": slo_availability,
                "sla_availability": sla_availability,
                "slo_status": slo_status,
                "sla_status": sla_status,
                "has_active_downtime": has_active_downtime,
                "cluster_domain": cluster_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.k8s_cluster_list_active_condition_instances_item import (
            K8SClusterListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.k8s_cluster_list_created import K8SClusterListCreated  # noqa: PLC0415
        from ..models.k8s_cluster_list_organization_type_0 import K8SClusterListOrganizationType0  # noqa: PLC0415
        from ..models.k8s_cluster_list_workspace_type_0 import K8SClusterListWorkspaceType0  # noqa: PLC0415

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
            active_condition_instances_item = K8SClusterListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> K8SClusterListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = K8SClusterListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> K8SClusterListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = K8SClusterListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(K8SClusterListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = K8SClusterListCreated.from_dict(d.pop("created"))

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

        kind = check_k8s_cluster_kind_enum(d.pop("kind"))

        installed = d.pop("installed")

        is_host_cluster = d.pop("is_host_cluster")

        is_infrastructure_cluster = d.pop("is_infrastructure_cluster")

        def _parse_kubernetes_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kubernetes_version = _parse_kubernetes_version(d.pop("kubernetes_version"))

        def _parse_kubeconfig_ca_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_ca_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_ca_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        kubeconfig_ca_cert_expiry_date = _parse_kubeconfig_ca_cert_expiry_date(d.pop("kubeconfig_ca_cert_expiry_date"))

        def _parse_kubeconfig_client_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kubeconfig_client_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return kubeconfig_client_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        kubeconfig_client_cert_expiry_date = _parse_kubeconfig_client_cert_expiry_date(
            d.pop("kubeconfig_client_cert_expiry_date")
        )

        def _parse_api_server_cert_expiry_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                api_server_cert_expiry_date_type_0 = datetime.datetime.fromisoformat(data)

                return api_server_cert_expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        api_server_cert_expiry_date = _parse_api_server_cert_expiry_date(d.pop("api_server_cert_expiry_date"))

        def _parse_credential(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        credential = _parse_credential(d.pop("credential"))

        slo_availability = d.pop("slo_availability")

        sla_availability = d.pop("sla_availability")

        slo_status = d.pop("slo_status")

        sla_status = d.pop("sla_status")

        has_active_downtime = d.pop("has_active_downtime")

        def _parse_cluster_domain(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cluster_domain = _parse_cluster_domain(d.pop("cluster_domain"))

        k8s_cluster_list = cls(
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
            kind=kind,
            installed=installed,
            is_host_cluster=is_host_cluster,
            is_infrastructure_cluster=is_infrastructure_cluster,
            kubernetes_version=kubernetes_version,
            kubeconfig_ca_cert_expiry_date=kubeconfig_ca_cert_expiry_date,
            kubeconfig_client_cert_expiry_date=kubeconfig_client_cert_expiry_date,
            api_server_cert_expiry_date=api_server_cert_expiry_date,
            credential=credential,
            slo_availability=slo_availability,
            sla_availability=sla_availability,
            slo_status=slo_status,
            sla_status=sla_status,
            has_active_downtime=has_active_downtime,
            cluster_domain=cluster_domain,
        )

        k8s_cluster_list.additional_properties = d
        return k8s_cluster_list

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
