from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.discount_type_enum import DiscountTypeEnum, check_discount_type_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.product_kind_enum import ProductKindEnum, check_product_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pricing_rule_list_active_condition_instances_item import PricingRuleListActiveConditionInstancesItem
    from ..models.pricing_rule_list_created import PricingRuleListCreated
    from ..models.pricing_rule_list_organization_type_0 import PricingRuleListOrganizationType0
    from ..models.pricing_rule_list_workspace_type_0 import PricingRuleListWorkspaceType0
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="PricingRuleList")


@_attrs_define
class PricingRuleList:
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
            active_condition_instances (list[PricingRuleListActiveConditionInstancesItem]):
            organization (None | PricingRuleListOrganizationType0):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | PricingRuleListWorkspaceType0):
            created (PricingRuleListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            product (ProductSimple): Compact serializer for embedding Product as FK reference.
            discount_type (DiscountTypeEnum): * `percentage` - Percentage
                * `fixed_override` - Fixed Override
                * `fixed_reduction` - Fixed Reduction
            discount_value (str):
            product_kind (BlankEnum | None | ProductKindEnum | Unset):
            active_from (datetime.date | None | Unset):
            active_until (datetime.date | None | Unset):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[PricingRuleListActiveConditionInstancesItem]
    organization: None | PricingRuleListOrganizationType0
    organization_priority: bool
    workspace: None | PricingRuleListWorkspaceType0
    created: PricingRuleListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    product: ProductSimple
    discount_type: DiscountTypeEnum
    discount_value: str
    product_kind: BlankEnum | None | ProductKindEnum | Unset = UNSET
    active_from: datetime.date | None | Unset = UNSET
    active_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pricing_rule_list_organization_type_0 import PricingRuleListOrganizationType0  # noqa: PLC0415
        from ..models.pricing_rule_list_workspace_type_0 import PricingRuleListWorkspaceType0  # noqa: PLC0415

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
        if isinstance(self.organization, PricingRuleListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, PricingRuleListWorkspaceType0):
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

        product = self.product.to_dict()

        discount_type: str = self.discount_type

        discount_value = self.discount_value

        product_kind: None | str | Unset
        if isinstance(self.product_kind, Unset):
            product_kind = UNSET
        elif isinstance(self.product_kind, str):
            product_kind = self.product_kind
        elif isinstance(self.product_kind, str):
            product_kind = self.product_kind
        else:
            product_kind = self.product_kind

        active_from: None | str | Unset
        if isinstance(self.active_from, Unset):
            active_from = UNSET
        elif isinstance(self.active_from, datetime.date):
            active_from = self.active_from.isoformat()
        else:
            active_from = self.active_from

        active_until: None | str | Unset
        if isinstance(self.active_until, Unset):
            active_until = UNSET
        elif isinstance(self.active_until, datetime.date):
            active_until = self.active_until.isoformat()
        else:
            active_until = self.active_until

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
                "product": product,
                "discount_type": discount_type,
                "discount_value": discount_value,
            }
        )
        if product_kind is not UNSET:
            field_dict["product_kind"] = product_kind
        if active_from is not UNSET:
            field_dict["active_from"] = active_from
        if active_until is not UNSET:
            field_dict["active_until"] = active_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pricing_rule_list_active_condition_instances_item import (
            PricingRuleListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.pricing_rule_list_created import PricingRuleListCreated  # noqa: PLC0415
        from ..models.pricing_rule_list_organization_type_0 import PricingRuleListOrganizationType0  # noqa: PLC0415
        from ..models.pricing_rule_list_workspace_type_0 import PricingRuleListWorkspaceType0  # noqa: PLC0415
        from ..models.product_simple import ProductSimple  # noqa: PLC0415

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
            active_condition_instances_item = PricingRuleListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | PricingRuleListOrganizationType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = PricingRuleListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PricingRuleListOrganizationType0, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | PricingRuleListWorkspaceType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = PricingRuleListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PricingRuleListWorkspaceType0, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = PricingRuleListCreated.from_dict(d.pop("created"))

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

        product = ProductSimple.from_dict(d.pop("product"))

        discount_type = check_discount_type_enum(d.pop("discount_type"))

        discount_value = d.pop("discount_value")

        def _parse_product_kind(data: object) -> BlankEnum | None | ProductKindEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_kind_type_0 = check_product_kind_enum(data)

                return product_kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_kind_type_1 = check_blank_enum(data)

                return product_kind_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | ProductKindEnum | Unset, data)

        product_kind = _parse_product_kind(d.pop("product_kind", UNSET))

        def _parse_active_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_from_type_0 = datetime.date.fromisoformat(data)

                return active_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_from = _parse_active_from(d.pop("active_from", UNSET))

        def _parse_active_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_until_type_0 = datetime.date.fromisoformat(data)

                return active_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        active_until = _parse_active_until(d.pop("active_until", UNSET))

        pricing_rule_list = cls(
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
            product=product,
            discount_type=discount_type,
            discount_value=discount_value,
            product_kind=product_kind,
            active_from=active_from,
            active_until=active_until,
        )

        pricing_rule_list.additional_properties = d
        return pricing_rule_list

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
