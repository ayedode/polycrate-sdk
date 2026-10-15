from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.registrar_tld_price_list_effective_criticality_type_1 import (
    RegistrarTLDPriceListEffectiveCriticalityType1,
    check_registrar_tld_price_list_effective_criticality_type_1,
)
from ..models.registrar_tld_price_list_effective_criticality_type_2_type_1 import (
    RegistrarTLDPriceListEffectiveCriticalityType2Type1,
    check_registrar_tld_price_list_effective_criticality_type_2_type_1,
)
from ..models.registrar_tld_price_list_effective_criticality_type_3_type_1 import (
    RegistrarTLDPriceListEffectiveCriticalityType3Type1,
    check_registrar_tld_price_list_effective_criticality_type_3_type_1,
)
from ..models.registrar_tld_price_list_state import RegistrarTLDPriceListState, check_registrar_tld_price_list_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_registrar_simple import DomainRegistrarSimple
    from ..models.registrar_tld_price_list_active_condition_instances_item import (
        RegistrarTLDPriceListActiveConditionInstancesItem,
    )
    from ..models.registrar_tld_price_list_created import RegistrarTLDPriceListCreated
    from ..models.registrar_tld_price_list_organization_type_0 import RegistrarTLDPriceListOrganizationType0
    from ..models.registrar_tld_price_list_workspace_type_0 import RegistrarTLDPriceListWorkspaceType0


T = TypeVar("T", bound="RegistrarTLDPriceList")


@_attrs_define
class RegistrarTLDPriceList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (RegistrarTLDPriceListState): * `OK` - Ok
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
            active_condition_instances (list[RegistrarTLDPriceListActiveConditionInstancesItem]):
            organization (None | RegistrarTLDPriceListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | RegistrarTLDPriceListWorkspaceType0):
            created (RegistrarTLDPriceListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (None | RegistrarTLDPriceListEffectiveCriticalityType1 |
                RegistrarTLDPriceListEffectiveCriticalityType2Type1 | RegistrarTLDPriceListEffectiveCriticalityType3Type1):
            url (str): Gibt die absolute URL zum Object zurück.
            tld (str): TLD without leading dot.
            registrar (DomainRegistrarSimple):
            active (bool | Unset): Staff switch: we sell this TLD. Sync never writes this field.
            offerable (bool | Unset): Informative OpenProvider list flag. Not the sales filter.
            vk_create (None | str | Unset):
            vk_renew (None | str | Unset):
            vk_transfer (None | str | Unset):
            vk_domicile (None | str | Unset):
            ek_create (None | str | Unset):
            ek_renew (None | str | Unset):
            currency (str | Unset):
    """

    id: UUID
    name: str
    state: RegistrarTLDPriceListState
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[RegistrarTLDPriceListActiveConditionInstancesItem]
    organization: None | RegistrarTLDPriceListOrganizationType0
    organization_priority: bool
    workspace: None | RegistrarTLDPriceListWorkspaceType0
    created: RegistrarTLDPriceListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: (
        None
        | RegistrarTLDPriceListEffectiveCriticalityType1
        | RegistrarTLDPriceListEffectiveCriticalityType2Type1
        | RegistrarTLDPriceListEffectiveCriticalityType3Type1
    )
    url: str
    tld: str
    registrar: DomainRegistrarSimple
    active: bool | Unset = UNSET
    offerable: bool | Unset = UNSET
    vk_create: None | str | Unset = UNSET
    vk_renew: None | str | Unset = UNSET
    vk_transfer: None | str | Unset = UNSET
    vk_domicile: None | str | Unset = UNSET
    ek_create: None | str | Unset = UNSET
    ek_renew: None | str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.registrar_tld_price_list_organization_type_0 import RegistrarTLDPriceListOrganizationType0  # noqa: PLC0415
        from ..models.registrar_tld_price_list_workspace_type_0 import RegistrarTLDPriceListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, RegistrarTLDPriceListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, RegistrarTLDPriceListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        tld = self.tld

        registrar = self.registrar.to_dict()

        active = self.active

        offerable = self.offerable

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

        currency = self.currency

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
                "tld": tld,
                "registrar": registrar,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if offerable is not UNSET:
            field_dict["offerable"] = offerable
        if vk_create is not UNSET:
            field_dict["vk_create"] = vk_create
        if vk_renew is not UNSET:
            field_dict["vk_renew"] = vk_renew
        if vk_transfer is not UNSET:
            field_dict["vk_transfer"] = vk_transfer
        if vk_domicile is not UNSET:
            field_dict["vk_domicile"] = vk_domicile
        if ek_create is not UNSET:
            field_dict["ek_create"] = ek_create
        if ek_renew is not UNSET:
            field_dict["ek_renew"] = ek_renew
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_registrar_simple import DomainRegistrarSimple  # noqa: PLC0415
        from ..models.registrar_tld_price_list_active_condition_instances_item import (
            RegistrarTLDPriceListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.registrar_tld_price_list_created import RegistrarTLDPriceListCreated  # noqa: PLC0415
        from ..models.registrar_tld_price_list_organization_type_0 import RegistrarTLDPriceListOrganizationType0  # noqa: PLC0415
        from ..models.registrar_tld_price_list_workspace_type_0 import RegistrarTLDPriceListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_registrar_tld_price_list_state(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = RegistrarTLDPriceListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | RegistrarTLDPriceListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = RegistrarTLDPriceListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | RegistrarTLDPriceListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = RegistrarTLDPriceListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegistrarTLDPriceListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = RegistrarTLDPriceListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceListEffectiveCriticalityType1
            | RegistrarTLDPriceListEffectiveCriticalityType2Type1
            | RegistrarTLDPriceListEffectiveCriticalityType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_registrar_tld_price_list_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = (
                    check_registrar_tld_price_list_effective_criticality_type_2_type_1(data)
                )

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = (
                    check_registrar_tld_price_list_effective_criticality_type_3_type_1(data)
                )

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceListEffectiveCriticalityType1
                | RegistrarTLDPriceListEffectiveCriticalityType2Type1
                | RegistrarTLDPriceListEffectiveCriticalityType3Type1,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        tld = d.pop("tld")

        registrar = DomainRegistrarSimple.from_dict(d.pop("registrar"))

        active = d.pop("active", UNSET)

        offerable = d.pop("offerable", UNSET)

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

        currency = d.pop("currency", UNSET)

        registrar_tld_price_list = cls(
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
            tld=tld,
            registrar=registrar,
            active=active,
            offerable=offerable,
            vk_create=vk_create,
            vk_renew=vk_renew,
            vk_transfer=vk_transfer,
            vk_domicile=vk_domicile,
            ek_create=ek_create,
            ek_renew=ek_renew,
            currency=currency,
        )

        registrar_tld_price_list.additional_properties = d
        return registrar_tld_price_list

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
