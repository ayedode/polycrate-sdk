from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.billing_interval_enum import BillingIntervalEnum, check_billing_interval_enum
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.product_kind_enum import ProductKindEnum, check_product_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductDetailRequest")


@_attrs_define
class ProductDetailRequest:
    """Full detail serializer.

    Attributes:
        kind (ProductKindEnum): * `host` - Host
            * `k8scluster` - K8s Cluster
            * `k8sapp` - K8s App
            * `support` - Support
            * `object-storage` - Object Storage
            * `block-storage` - Block Storage
            * `loadbalancer` - Loadbalancer
            * `project` - Project
            * `dnszone` - DNS Zone
            * `assistant` - Assistant
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
        billing_interval (BillingIntervalEnum | Unset): * `second` - Second
            * `minute` - Minute
            * `hour` - Hour
            * `day` - Day
            * `month` - Month
            * `year` - Year
        price_per_unit (None | str | Unset):
        cost_per_unit (None | str | Unset):
        provider_entity (None | Unset | UUID):
        pop (None | Unset | UUID): Concrete IaaS location (e.g. hetzner-fsn1). Location slug is the PoP name suffix.
        provider_type_id (None | str | Unset):
        config (Any | Unset):
    """

    kind: ProductKindEnum
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
    billing_interval: BillingIntervalEnum | Unset = UNSET
    price_per_unit: None | str | Unset = UNSET
    cost_per_unit: None | str | Unset = UNSET
    provider_entity: None | Unset | UUID = UNSET
    pop: None | Unset | UUID = UNSET
    provider_type_id: None | str | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

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

        billing_interval: str | Unset = UNSET
        if not isinstance(self.billing_interval, Unset):
            billing_interval = self.billing_interval

        price_per_unit: None | str | Unset
        if isinstance(self.price_per_unit, Unset):
            price_per_unit = UNSET
        else:
            price_per_unit = self.price_per_unit

        cost_per_unit: None | str | Unset
        if isinstance(self.cost_per_unit, Unset):
            cost_per_unit = UNSET
        else:
            cost_per_unit = self.cost_per_unit

        provider_entity: None | str | Unset
        if isinstance(self.provider_entity, Unset):
            provider_entity = UNSET
        elif isinstance(self.provider_entity, UUID):
            provider_entity = str(self.provider_entity)
        else:
            provider_entity = self.provider_entity

        pop: None | str | Unset
        if isinstance(self.pop, Unset):
            pop = UNSET
        elif isinstance(self.pop, UUID):
            pop = str(self.pop)
        else:
            pop = self.pop

        provider_type_id: None | str | Unset
        if isinstance(self.provider_type_id, Unset):
            provider_type_id = UNSET
        else:
            provider_type_id = self.provider_type_id

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
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
        if billing_interval is not UNSET:
            field_dict["billing_interval"] = billing_interval
        if price_per_unit is not UNSET:
            field_dict["price_per_unit"] = price_per_unit
        if cost_per_unit is not UNSET:
            field_dict["cost_per_unit"] = cost_per_unit
        if provider_entity is not UNSET:
            field_dict["provider_entity"] = provider_entity
        if pop is not UNSET:
            field_dict["pop"] = pop
        if provider_type_id is not UNSET:
            field_dict["provider_type_id"] = provider_type_id
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

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

        if not isinstance(self.billing_interval, Unset):
            files.append(("billing_interval", (None, str(self.billing_interval).encode(), "text/plain")))

        if not isinstance(self.price_per_unit, Unset):
            if isinstance(self.price_per_unit, str):
                files.append(("price_per_unit", (None, str(self.price_per_unit).encode(), "text/plain")))
            else:
                files.append(("price_per_unit", (None, str(self.price_per_unit).encode(), "text/plain")))

        if not isinstance(self.cost_per_unit, Unset):
            if isinstance(self.cost_per_unit, str):
                files.append(("cost_per_unit", (None, str(self.cost_per_unit).encode(), "text/plain")))
            else:
                files.append(("cost_per_unit", (None, str(self.cost_per_unit).encode(), "text/plain")))

        if not isinstance(self.provider_entity, Unset):
            if isinstance(self.provider_entity, UUID):
                files.append(("provider_entity", (None, str(self.provider_entity), "text/plain")))
            else:
                files.append(("provider_entity", (None, str(self.provider_entity).encode(), "text/plain")))

        if not isinstance(self.pop, Unset):
            if isinstance(self.pop, UUID):
                files.append(("pop", (None, str(self.pop), "text/plain")))
            else:
                files.append(("pop", (None, str(self.pop).encode(), "text/plain")))

        if not isinstance(self.provider_type_id, Unset):
            if isinstance(self.provider_type_id, str):
                files.append(("provider_type_id", (None, str(self.provider_type_id).encode(), "text/plain")))
            else:
                files.append(("provider_type_id", (None, str(self.provider_type_id).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_product_kind_enum(d.pop("kind"))

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

        _billing_interval = d.pop("billing_interval", UNSET)
        billing_interval: BillingIntervalEnum | Unset
        if isinstance(_billing_interval, Unset):
            billing_interval = UNSET
        else:
            billing_interval = check_billing_interval_enum(_billing_interval)

        def _parse_price_per_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_per_unit = _parse_price_per_unit(d.pop("price_per_unit", UNSET))

        def _parse_cost_per_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_per_unit = _parse_cost_per_unit(d.pop("cost_per_unit", UNSET))

        def _parse_provider_entity(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_entity_type_0 = UUID(data)

                return provider_entity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        provider_entity = _parse_provider_entity(d.pop("provider_entity", UNSET))

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

        def _parse_provider_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_type_id = _parse_provider_type_id(d.pop("provider_type_id", UNSET))

        config = d.pop("config", UNSET)

        product_detail_request = cls(
            kind=kind,
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
            billing_interval=billing_interval,
            price_per_unit=price_per_unit,
            cost_per_unit=cost_per_unit,
            provider_entity=provider_entity,
            pop=pop,
            provider_type_id=provider_type_id,
            config=config,
        )

        product_detail_request.additional_properties = d
        return product_detail_request

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
