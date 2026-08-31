from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_products_update_annotations_error_component import (
        ApiV1PricingProductsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_archived_at_error_component import (
        ApiV1PricingProductsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_archived_error_component import (
        ApiV1PricingProductsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_archived_reason_error_component import (
        ApiV1PricingProductsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_billing_interval_error_component import (
        ApiV1PricingProductsUpdateBillingIntervalErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_config_error_component import (
        ApiV1PricingProductsUpdateConfigErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_cost_per_unit_error_component import (
        ApiV1PricingProductsUpdateCostPerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_criticality_error_component import (
        ApiV1PricingProductsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_debug_mode_error_component import (
        ApiV1PricingProductsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_display_name_error_component import (
        ApiV1PricingProductsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_kind_error_component import (
        ApiV1PricingProductsUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_labels_error_component import (
        ApiV1PricingProductsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_name_error_component import (
        ApiV1PricingProductsUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_non_field_errors_error_component import (
        ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_platform_service_error_component import (
        ApiV1PricingProductsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_price_per_unit_error_component import (
        ApiV1PricingProductsUpdatePricePerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_provider_entity_error_component import (
        ApiV1PricingProductsUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_provider_error_component import (
        ApiV1PricingProductsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_provider_id_error_component import (
        ApiV1PricingProductsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_provider_reference_error_component import (
        ApiV1PricingProductsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_provider_type_id_error_component import (
        ApiV1PricingProductsUpdateProviderTypeIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_reconciliation_enabled_error_component import (
        ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_sla_availability_error_component import (
        ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_sla_target_error_component import (
        ApiV1PricingProductsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_slo_availability_error_component import (
        ApiV1PricingProductsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_slo_target_error_component import (
        ApiV1PricingProductsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_target_availability_error_component import (
        ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_update_tolerations_error_component import (
        ApiV1PricingProductsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingProductsUpdateValidationError")


@_attrs_define
class ApiV1PricingProductsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingProductsUpdateAnnotationsErrorComponent |
            ApiV1PricingProductsUpdateArchivedAtErrorComponent | ApiV1PricingProductsUpdateArchivedErrorComponent |
            ApiV1PricingProductsUpdateArchivedReasonErrorComponent | ApiV1PricingProductsUpdateBillingIntervalErrorComponent
            | ApiV1PricingProductsUpdateConfigErrorComponent | ApiV1PricingProductsUpdateCostPerUnitErrorComponent |
            ApiV1PricingProductsUpdateCriticalityErrorComponent | ApiV1PricingProductsUpdateDebugModeErrorComponent |
            ApiV1PricingProductsUpdateDisplayNameErrorComponent | ApiV1PricingProductsUpdateKindErrorComponent |
            ApiV1PricingProductsUpdateLabelsErrorComponent | ApiV1PricingProductsUpdateNameErrorComponent |
            ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent | ApiV1PricingProductsUpdatePlatformServiceErrorComponent
            | ApiV1PricingProductsUpdatePricePerUnitErrorComponent | ApiV1PricingProductsUpdateProviderEntityErrorComponent
            | ApiV1PricingProductsUpdateProviderErrorComponent | ApiV1PricingProductsUpdateProviderIdErrorComponent |
            ApiV1PricingProductsUpdateProviderReferenceErrorComponent |
            ApiV1PricingProductsUpdateProviderTypeIdErrorComponent |
            ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent | ApiV1PricingProductsUpdateSlaTargetErrorComponent |
            ApiV1PricingProductsUpdateSloAvailabilityErrorComponent | ApiV1PricingProductsUpdateSloTargetErrorComponent |
            ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingProductsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingProductsUpdateAnnotationsErrorComponent
        | ApiV1PricingProductsUpdateArchivedAtErrorComponent
        | ApiV1PricingProductsUpdateArchivedErrorComponent
        | ApiV1PricingProductsUpdateArchivedReasonErrorComponent
        | ApiV1PricingProductsUpdateBillingIntervalErrorComponent
        | ApiV1PricingProductsUpdateConfigErrorComponent
        | ApiV1PricingProductsUpdateCostPerUnitErrorComponent
        | ApiV1PricingProductsUpdateCriticalityErrorComponent
        | ApiV1PricingProductsUpdateDebugModeErrorComponent
        | ApiV1PricingProductsUpdateDisplayNameErrorComponent
        | ApiV1PricingProductsUpdateKindErrorComponent
        | ApiV1PricingProductsUpdateLabelsErrorComponent
        | ApiV1PricingProductsUpdateNameErrorComponent
        | ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingProductsUpdatePlatformServiceErrorComponent
        | ApiV1PricingProductsUpdatePricePerUnitErrorComponent
        | ApiV1PricingProductsUpdateProviderEntityErrorComponent
        | ApiV1PricingProductsUpdateProviderErrorComponent
        | ApiV1PricingProductsUpdateProviderIdErrorComponent
        | ApiV1PricingProductsUpdateProviderReferenceErrorComponent
        | ApiV1PricingProductsUpdateProviderTypeIdErrorComponent
        | ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingProductsUpdateSlaTargetErrorComponent
        | ApiV1PricingProductsUpdateSloAvailabilityErrorComponent
        | ApiV1PricingProductsUpdateSloTargetErrorComponent
        | ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingProductsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_products_update_annotations_error_component import (
            ApiV1PricingProductsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_at_error_component import (
            ApiV1PricingProductsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_error_component import (
            ApiV1PricingProductsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_reason_error_component import (
            ApiV1PricingProductsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_billing_interval_error_component import (
            ApiV1PricingProductsUpdateBillingIntervalErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_cost_per_unit_error_component import (
            ApiV1PricingProductsUpdateCostPerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_criticality_error_component import (
            ApiV1PricingProductsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_debug_mode_error_component import (
            ApiV1PricingProductsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_display_name_error_component import (
            ApiV1PricingProductsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_kind_error_component import (
            ApiV1PricingProductsUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_labels_error_component import (
            ApiV1PricingProductsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_name_error_component import (
            ApiV1PricingProductsUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_non_field_errors_error_component import (
            ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_platform_service_error_component import (
            ApiV1PricingProductsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_price_per_unit_error_component import (
            ApiV1PricingProductsUpdatePricePerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_entity_error_component import (
            ApiV1PricingProductsUpdateProviderEntityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_error_component import (
            ApiV1PricingProductsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_id_error_component import (
            ApiV1PricingProductsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_reference_error_component import (
            ApiV1PricingProductsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_type_id_error_component import (
            ApiV1PricingProductsUpdateProviderTypeIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_reconciliation_enabled_error_component import (
            ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_sla_availability_error_component import (
            ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_sla_target_error_component import (
            ApiV1PricingProductsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_slo_availability_error_component import (
            ApiV1PricingProductsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_slo_target_error_component import (
            ApiV1PricingProductsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_target_availability_error_component import (
            ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_tolerations_error_component import (
            ApiV1PricingProductsUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateBillingIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdatePricePerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateCostPerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsUpdateProviderTypeIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_pricing_products_update_annotations_error_component import (
            ApiV1PricingProductsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_at_error_component import (
            ApiV1PricingProductsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_error_component import (
            ApiV1PricingProductsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_archived_reason_error_component import (
            ApiV1PricingProductsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_billing_interval_error_component import (
            ApiV1PricingProductsUpdateBillingIntervalErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_config_error_component import (
            ApiV1PricingProductsUpdateConfigErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_cost_per_unit_error_component import (
            ApiV1PricingProductsUpdateCostPerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_criticality_error_component import (
            ApiV1PricingProductsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_debug_mode_error_component import (
            ApiV1PricingProductsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_display_name_error_component import (
            ApiV1PricingProductsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_kind_error_component import (
            ApiV1PricingProductsUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_labels_error_component import (
            ApiV1PricingProductsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_name_error_component import (
            ApiV1PricingProductsUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_non_field_errors_error_component import (
            ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_platform_service_error_component import (
            ApiV1PricingProductsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_price_per_unit_error_component import (
            ApiV1PricingProductsUpdatePricePerUnitErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_entity_error_component import (
            ApiV1PricingProductsUpdateProviderEntityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_error_component import (
            ApiV1PricingProductsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_id_error_component import (
            ApiV1PricingProductsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_reference_error_component import (
            ApiV1PricingProductsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_provider_type_id_error_component import (
            ApiV1PricingProductsUpdateProviderTypeIdErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_reconciliation_enabled_error_component import (
            ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_sla_availability_error_component import (
            ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_sla_target_error_component import (
            ApiV1PricingProductsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_slo_availability_error_component import (
            ApiV1PricingProductsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_slo_target_error_component import (
            ApiV1PricingProductsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_target_availability_error_component import (
            ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_products_update_tolerations_error_component import (
            ApiV1PricingProductsUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingProductsUpdateAnnotationsErrorComponent
                | ApiV1PricingProductsUpdateArchivedAtErrorComponent
                | ApiV1PricingProductsUpdateArchivedErrorComponent
                | ApiV1PricingProductsUpdateArchivedReasonErrorComponent
                | ApiV1PricingProductsUpdateBillingIntervalErrorComponent
                | ApiV1PricingProductsUpdateConfigErrorComponent
                | ApiV1PricingProductsUpdateCostPerUnitErrorComponent
                | ApiV1PricingProductsUpdateCriticalityErrorComponent
                | ApiV1PricingProductsUpdateDebugModeErrorComponent
                | ApiV1PricingProductsUpdateDisplayNameErrorComponent
                | ApiV1PricingProductsUpdateKindErrorComponent
                | ApiV1PricingProductsUpdateLabelsErrorComponent
                | ApiV1PricingProductsUpdateNameErrorComponent
                | ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingProductsUpdatePlatformServiceErrorComponent
                | ApiV1PricingProductsUpdatePricePerUnitErrorComponent
                | ApiV1PricingProductsUpdateProviderEntityErrorComponent
                | ApiV1PricingProductsUpdateProviderErrorComponent
                | ApiV1PricingProductsUpdateProviderIdErrorComponent
                | ApiV1PricingProductsUpdateProviderReferenceErrorComponent
                | ApiV1PricingProductsUpdateProviderTypeIdErrorComponent
                | ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingProductsUpdateSlaTargetErrorComponent
                | ApiV1PricingProductsUpdateSloAvailabilityErrorComponent
                | ApiV1PricingProductsUpdateSloTargetErrorComponent
                | ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingProductsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_0 = (
                        ApiV1PricingProductsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_1 = (
                        ApiV1PricingProductsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_2 = (
                        ApiV1PricingProductsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_3 = (
                        ApiV1PricingProductsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_4 = (
                        ApiV1PricingProductsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_5 = (
                        ApiV1PricingProductsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_6 = (
                        ApiV1PricingProductsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_7 = (
                        ApiV1PricingProductsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_8 = (
                        ApiV1PricingProductsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_9 = (
                        ApiV1PricingProductsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_10 = (
                        ApiV1PricingProductsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_11 = (
                        ApiV1PricingProductsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_12 = (
                        ApiV1PricingProductsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_13 = (
                        ApiV1PricingProductsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_14 = (
                        ApiV1PricingProductsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_15 = (
                        ApiV1PricingProductsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_16 = (
                        ApiV1PricingProductsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_17 = (
                        ApiV1PricingProductsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_18 = (
                        ApiV1PricingProductsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_19 = (
                        ApiV1PricingProductsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_20 = (
                        ApiV1PricingProductsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_21 = (
                        ApiV1PricingProductsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_22 = (
                        ApiV1PricingProductsUpdateBillingIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_23 = (
                        ApiV1PricingProductsUpdatePricePerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_24 = (
                        ApiV1PricingProductsUpdateCostPerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_25 = (
                        ApiV1PricingProductsUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_update_error_type_26 = (
                        ApiV1PricingProductsUpdateProviderTypeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_products_update_error_type_27 = (
                    ApiV1PricingProductsUpdateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_products_update_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_products_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_products_update_validation_error.additional_properties = d
        return api_v1_pricing_products_update_validation_error

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
