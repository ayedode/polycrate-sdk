from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_public_list_billing_interval import (
    ProductPublicListBillingInterval,
    check_product_public_list_billing_interval,
)
from ..models.product_public_list_effective_criticality_type_1 import (
    ProductPublicListEffectiveCriticalityType1,
    check_product_public_list_effective_criticality_type_1,
)
from ..models.product_public_list_effective_criticality_type_2_type_1 import (
    ProductPublicListEffectiveCriticalityType2Type1,
    check_product_public_list_effective_criticality_type_2_type_1,
)
from ..models.product_public_list_effective_criticality_type_3_type_1 import (
    ProductPublicListEffectiveCriticalityType3Type1,
    check_product_public_list_effective_criticality_type_3_type_1,
)
from ..models.product_public_list_kind import ProductPublicListKind, check_product_public_list_kind
from ..models.product_public_list_state import ProductPublicListState, check_product_public_list_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_public_list_active_condition_instances_item import (
        ProductPublicListActiveConditionInstancesItem,
    )
    from ..models.product_public_list_created import ProductPublicListCreated
    from ..models.product_public_list_organization_type_0 import ProductPublicListOrganizationType0
    from ..models.product_public_list_workspace_type_0 import ProductPublicListWorkspaceType0


T = TypeVar("T", bound="ProductPublicList")


@_attrs_define
class ProductPublicList:
    """Anonymous / non-staff list. Omits internal purchase cost (Spec 866).

    Attributes:
        id (UUID):
        name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
        state (ProductPublicListState): * `OK` - Ok
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
        active_condition_instances (list[ProductPublicListActiveConditionInstancesItem]):
        organization (None | ProductPublicListOrganizationType0):
        organization_priority (bool): True when the object's organization has priority=True.
        workspace (None | ProductPublicListWorkspaceType0):
        created (ProductPublicListCreated):
        archived (bool): Archived objects are not shown in the UI and are not managed by the API.
        reconciliation_running (bool):
        effective_criticality (None | ProductPublicListEffectiveCriticalityType1 |
            ProductPublicListEffectiveCriticalityType2Type1 | ProductPublicListEffectiveCriticalityType3Type1):
        url (str): Gibt die absolute URL zum Object zurück.
        kind (ProductPublicListKind): * `host` - Host
            * `k8scluster` - K8s Cluster
            * `k8sapp` - K8s App
            * `support` - Support
            * `object-storage` - Object Storage
            * `block-storage` - Block Storage
            * `loadbalancer` - Loadbalancer
            * `project` - Project
            * `dnszone` - DNS Zone
            * `assistant` - Assistant
            * `registry-storage` - Registry Storage
            * `secrets-namespace` - Secrets Namespace
            * `endpoint-monitor` - Endpoint Monitor
            * `domain` - Domain
        billing_interval (ProductPublicListBillingInterval | Unset): * `second` - Second
            * `minute` - Minute
            * `hour` - Hour
            * `day` - Day
            * `month` - Month
            * `year` - Year
        price_per_unit (None | str | Unset):
        provider_type_id (None | str | Unset):
        pop (None | Unset | UUID): Concrete IaaS location (e.g. hetzner-fsn1). Location slug is the PoP name suffix.
        region (None | Unset | UUID): Platform Region for broker Host SKUs (Spec 938). Location from
            region.workspace.pop.
    """

    id: UUID
    name: str
    state: ProductPublicListState
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ProductPublicListActiveConditionInstancesItem]
    organization: None | ProductPublicListOrganizationType0
    organization_priority: bool
    workspace: None | ProductPublicListWorkspaceType0
    created: ProductPublicListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: (
        None
        | ProductPublicListEffectiveCriticalityType1
        | ProductPublicListEffectiveCriticalityType2Type1
        | ProductPublicListEffectiveCriticalityType3Type1
    )
    url: str
    kind: ProductPublicListKind
    billing_interval: ProductPublicListBillingInterval | Unset = UNSET
    price_per_unit: None | str | Unset = UNSET
    provider_type_id: None | str | Unset = UNSET
    pop: None | Unset | UUID = UNSET
    region: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_public_list_organization_type_0 import ProductPublicListOrganizationType0  # noqa: PLC0415
        from ..models.product_public_list_workspace_type_0 import ProductPublicListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, ProductPublicListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ProductPublicListWorkspaceType0):
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

        kind: str = self.kind

        billing_interval: str | Unset = UNSET
        if not isinstance(self.billing_interval, Unset):
            billing_interval = self.billing_interval

        price_per_unit: None | str | Unset
        if isinstance(self.price_per_unit, Unset):
            price_per_unit = UNSET
        else:
            price_per_unit = self.price_per_unit

        provider_type_id: None | str | Unset
        if isinstance(self.provider_type_id, Unset):
            provider_type_id = UNSET
        else:
            provider_type_id = self.provider_type_id

        pop: None | str | Unset
        if isinstance(self.pop, Unset):
            pop = UNSET
        elif isinstance(self.pop, UUID):
            pop = str(self.pop)
        else:
            pop = self.pop

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, UUID):
            region = str(self.region)
        else:
            region = self.region

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
            }
        )
        if billing_interval is not UNSET:
            field_dict["billing_interval"] = billing_interval
        if price_per_unit is not UNSET:
            field_dict["price_per_unit"] = price_per_unit
        if provider_type_id is not UNSET:
            field_dict["provider_type_id"] = provider_type_id
        if pop is not UNSET:
            field_dict["pop"] = pop
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_public_list_active_condition_instances_item import (
            ProductPublicListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.product_public_list_created import ProductPublicListCreated  # noqa: PLC0415
        from ..models.product_public_list_organization_type_0 import ProductPublicListOrganizationType0  # noqa: PLC0415
        from ..models.product_public_list_workspace_type_0 import ProductPublicListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_product_public_list_state(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = ProductPublicListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | ProductPublicListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ProductPublicListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductPublicListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | ProductPublicListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ProductPublicListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductPublicListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ProductPublicListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            None
            | ProductPublicListEffectiveCriticalityType1
            | ProductPublicListEffectiveCriticalityType2Type1
            | ProductPublicListEffectiveCriticalityType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_product_public_list_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_product_public_list_effective_criticality_type_2_type_1(
                    data
                )

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_product_public_list_effective_criticality_type_3_type_1(
                    data
                )

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | ProductPublicListEffectiveCriticalityType1
                | ProductPublicListEffectiveCriticalityType2Type1
                | ProductPublicListEffectiveCriticalityType3Type1,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        kind = check_product_public_list_kind(d.pop("kind"))

        _billing_interval = d.pop("billing_interval", UNSET)
        billing_interval: ProductPublicListBillingInterval | Unset
        if isinstance(_billing_interval, Unset):
            billing_interval = UNSET
        else:
            billing_interval = check_product_public_list_billing_interval(_billing_interval)

        def _parse_price_per_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_per_unit = _parse_price_per_unit(d.pop("price_per_unit", UNSET))

        def _parse_provider_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_type_id = _parse_provider_type_id(d.pop("provider_type_id", UNSET))

        def _parse_pop(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pop_type_0 = UUID(data)

                return pop_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        pop = _parse_pop(d.pop("pop", UNSET))

        def _parse_region(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                region_type_0 = UUID(data)

                return region_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        region = _parse_region(d.pop("region", UNSET))

        product_public_list = cls(
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
            billing_interval=billing_interval,
            price_per_unit=price_per_unit,
            provider_type_id=provider_type_id,
            pop=pop,
            region=region,
        )

        product_public_list.additional_properties = d
        return product_public_list

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
