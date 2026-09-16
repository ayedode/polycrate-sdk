from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_products_create_annotations_error_component import (
        ApiV1PricingProductsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_archived_at_error_component import (
        ApiV1PricingProductsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_archived_error_component import (
        ApiV1PricingProductsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_archived_reason_error_component import (
        ApiV1PricingProductsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_billing_interval_error_component import (
        ApiV1PricingProductsCreateBillingIntervalErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_config_error_component import (
        ApiV1PricingProductsCreateConfigErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_cost_per_unit_error_component import (
        ApiV1PricingProductsCreateCostPerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_criticality_error_component import (
        ApiV1PricingProductsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_debug_mode_error_component import (
        ApiV1PricingProductsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_display_name_error_component import (
        ApiV1PricingProductsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_kind_error_component import (
        ApiV1PricingProductsCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_labels_error_component import (
        ApiV1PricingProductsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_name_error_component import (
        ApiV1PricingProductsCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_non_field_errors_error_component import (
        ApiV1PricingProductsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_platform_service_error_component import (
        ApiV1PricingProductsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_pop_error_component import ApiV1PricingProductsCreatePopErrorComponent
    from ..models.api_v1_pricing_products_create_price_per_unit_error_component import (
        ApiV1PricingProductsCreatePricePerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_provider_entity_error_component import (
        ApiV1PricingProductsCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_provider_error_component import (
        ApiV1PricingProductsCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_provider_id_error_component import (
        ApiV1PricingProductsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_provider_reference_error_component import (
        ApiV1PricingProductsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_provider_type_id_error_component import (
        ApiV1PricingProductsCreateProviderTypeIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_reconciliation_enabled_error_component import (
        ApiV1PricingProductsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_sla_availability_error_component import (
        ApiV1PricingProductsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_sla_target_error_component import (
        ApiV1PricingProductsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_slo_availability_error_component import (
        ApiV1PricingProductsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_slo_target_error_component import (
        ApiV1PricingProductsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_target_availability_error_component import (
        ApiV1PricingProductsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_create_tolerations_error_component import (
        ApiV1PricingProductsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingProductsCreateValidationError")


@_attrs_define
class ApiV1PricingProductsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingProductsCreateAnnotationsErrorComponent |
            ApiV1PricingProductsCreateArchivedAtErrorComponent | ApiV1PricingProductsCreateArchivedErrorComponent |
            ApiV1PricingProductsCreateArchivedReasonErrorComponent | ApiV1PricingProductsCreateBillingIntervalErrorComponent
            | ApiV1PricingProductsCreateConfigErrorComponent | ApiV1PricingProductsCreateCostPerUnitErrorComponent |
            ApiV1PricingProductsCreateCriticalityErrorComponent | ApiV1PricingProductsCreateDebugModeErrorComponent |
            ApiV1PricingProductsCreateDisplayNameErrorComponent | ApiV1PricingProductsCreateKindErrorComponent |
            ApiV1PricingProductsCreateLabelsErrorComponent | ApiV1PricingProductsCreateNameErrorComponent |
            ApiV1PricingProductsCreateNonFieldErrorsErrorComponent | ApiV1PricingProductsCreatePlatformServiceErrorComponent
            | ApiV1PricingProductsCreatePopErrorComponent | ApiV1PricingProductsCreatePricePerUnitErrorComponent |
            ApiV1PricingProductsCreateProviderEntityErrorComponent | ApiV1PricingProductsCreateProviderErrorComponent |
            ApiV1PricingProductsCreateProviderIdErrorComponent | ApiV1PricingProductsCreateProviderReferenceErrorComponent |
            ApiV1PricingProductsCreateProviderTypeIdErrorComponent |
            ApiV1PricingProductsCreateReconciliationEnabledErrorComponent |
            ApiV1PricingProductsCreateSlaAvailabilityErrorComponent | ApiV1PricingProductsCreateSlaTargetErrorComponent |
            ApiV1PricingProductsCreateSloAvailabilityErrorComponent | ApiV1PricingProductsCreateSloTargetErrorComponent |
            ApiV1PricingProductsCreateTargetAvailabilityErrorComponent |
            ApiV1PricingProductsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingProductsCreateAnnotationsErrorComponent
        | ApiV1PricingProductsCreateArchivedAtErrorComponent
        | ApiV1PricingProductsCreateArchivedErrorComponent
        | ApiV1PricingProductsCreateArchivedReasonErrorComponent
        | ApiV1PricingProductsCreateBillingIntervalErrorComponent
        | ApiV1PricingProductsCreateConfigErrorComponent
        | ApiV1PricingProductsCreateCostPerUnitErrorComponent
        | ApiV1PricingProductsCreateCriticalityErrorComponent
        | ApiV1PricingProductsCreateDebugModeErrorComponent
        | ApiV1PricingProductsCreateDisplayNameErrorComponent
        | ApiV1PricingProductsCreateKindErrorComponent
        | ApiV1PricingProductsCreateLabelsErrorComponent
        | ApiV1PricingProductsCreateNameErrorComponent
        | ApiV1PricingProductsCreateNonFieldErrorsErrorComponent
        | ApiV1PricingProductsCreatePlatformServiceErrorComponent
        | ApiV1PricingProductsCreatePopErrorComponent
        | ApiV1PricingProductsCreatePricePerUnitErrorComponent
        | ApiV1PricingProductsCreateProviderEntityErrorComponent
        | ApiV1PricingProductsCreateProviderErrorComponent
        | ApiV1PricingProductsCreateProviderIdErrorComponent
        | ApiV1PricingProductsCreateProviderReferenceErrorComponent
        | ApiV1PricingProductsCreateProviderTypeIdErrorComponent
        | ApiV1PricingProductsCreateReconciliationEnabledErrorComponent
        | ApiV1PricingProductsCreateSlaAvailabilityErrorComponent
        | ApiV1PricingProductsCreateSlaTargetErrorComponent
        | ApiV1PricingProductsCreateSloAvailabilityErrorComponent
        | ApiV1PricingProductsCreateSloTargetErrorComponent
        | ApiV1PricingProductsCreateTargetAvailabilityErrorComponent
        | ApiV1PricingProductsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_products_create_annotations_error_component import (
            ApiV1PricingProductsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_at_error_component import (
            ApiV1PricingProductsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_error_component import (
            ApiV1PricingProductsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_reason_error_component import (
            ApiV1PricingProductsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_billing_interval_error_component import (
            ApiV1PricingProductsCreateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_cost_per_unit_error_component import (
            ApiV1PricingProductsCreateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_criticality_error_component import (
            ApiV1PricingProductsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_debug_mode_error_component import (
            ApiV1PricingProductsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_display_name_error_component import (
            ApiV1PricingProductsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_kind_error_component import (
            ApiV1PricingProductsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_labels_error_component import (
            ApiV1PricingProductsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_name_error_component import (
            ApiV1PricingProductsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_non_field_errors_error_component import (
            ApiV1PricingProductsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_platform_service_error_component import (
            ApiV1PricingProductsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_pop_error_component import (
            ApiV1PricingProductsCreatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_price_per_unit_error_component import (
            ApiV1PricingProductsCreatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_entity_error_component import (
            ApiV1PricingProductsCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_error_component import (
            ApiV1PricingProductsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_id_error_component import (
            ApiV1PricingProductsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_reference_error_component import (
            ApiV1PricingProductsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_type_id_error_component import (
            ApiV1PricingProductsCreateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_sla_availability_error_component import (
            ApiV1PricingProductsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_sla_target_error_component import (
            ApiV1PricingProductsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_slo_availability_error_component import (
            ApiV1PricingProductsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_slo_target_error_component import (
            ApiV1PricingProductsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_target_availability_error_component import (
            ApiV1PricingProductsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_tolerations_error_component import (
            ApiV1PricingProductsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingProductsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateBillingIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreatePricePerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateCostPerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreatePopErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsCreateProviderTypeIdErrorComponent):
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
        from ..models.api_v1_pricing_products_create_annotations_error_component import (
            ApiV1PricingProductsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_at_error_component import (
            ApiV1PricingProductsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_error_component import (
            ApiV1PricingProductsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_archived_reason_error_component import (
            ApiV1PricingProductsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_billing_interval_error_component import (
            ApiV1PricingProductsCreateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_config_error_component import (
            ApiV1PricingProductsCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_cost_per_unit_error_component import (
            ApiV1PricingProductsCreateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_criticality_error_component import (
            ApiV1PricingProductsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_debug_mode_error_component import (
            ApiV1PricingProductsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_display_name_error_component import (
            ApiV1PricingProductsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_kind_error_component import (
            ApiV1PricingProductsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_labels_error_component import (
            ApiV1PricingProductsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_name_error_component import (
            ApiV1PricingProductsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_non_field_errors_error_component import (
            ApiV1PricingProductsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_platform_service_error_component import (
            ApiV1PricingProductsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_pop_error_component import (
            ApiV1PricingProductsCreatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_price_per_unit_error_component import (
            ApiV1PricingProductsCreatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_entity_error_component import (
            ApiV1PricingProductsCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_error_component import (
            ApiV1PricingProductsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_id_error_component import (
            ApiV1PricingProductsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_reference_error_component import (
            ApiV1PricingProductsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_provider_type_id_error_component import (
            ApiV1PricingProductsCreateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_sla_availability_error_component import (
            ApiV1PricingProductsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_sla_target_error_component import (
            ApiV1PricingProductsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_slo_availability_error_component import (
            ApiV1PricingProductsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_slo_target_error_component import (
            ApiV1PricingProductsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_target_availability_error_component import (
            ApiV1PricingProductsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_create_tolerations_error_component import (
            ApiV1PricingProductsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingProductsCreateAnnotationsErrorComponent
                | ApiV1PricingProductsCreateArchivedAtErrorComponent
                | ApiV1PricingProductsCreateArchivedErrorComponent
                | ApiV1PricingProductsCreateArchivedReasonErrorComponent
                | ApiV1PricingProductsCreateBillingIntervalErrorComponent
                | ApiV1PricingProductsCreateConfigErrorComponent
                | ApiV1PricingProductsCreateCostPerUnitErrorComponent
                | ApiV1PricingProductsCreateCriticalityErrorComponent
                | ApiV1PricingProductsCreateDebugModeErrorComponent
                | ApiV1PricingProductsCreateDisplayNameErrorComponent
                | ApiV1PricingProductsCreateKindErrorComponent
                | ApiV1PricingProductsCreateLabelsErrorComponent
                | ApiV1PricingProductsCreateNameErrorComponent
                | ApiV1PricingProductsCreateNonFieldErrorsErrorComponent
                | ApiV1PricingProductsCreatePlatformServiceErrorComponent
                | ApiV1PricingProductsCreatePopErrorComponent
                | ApiV1PricingProductsCreatePricePerUnitErrorComponent
                | ApiV1PricingProductsCreateProviderEntityErrorComponent
                | ApiV1PricingProductsCreateProviderErrorComponent
                | ApiV1PricingProductsCreateProviderIdErrorComponent
                | ApiV1PricingProductsCreateProviderReferenceErrorComponent
                | ApiV1PricingProductsCreateProviderTypeIdErrorComponent
                | ApiV1PricingProductsCreateReconciliationEnabledErrorComponent
                | ApiV1PricingProductsCreateSlaAvailabilityErrorComponent
                | ApiV1PricingProductsCreateSlaTargetErrorComponent
                | ApiV1PricingProductsCreateSloAvailabilityErrorComponent
                | ApiV1PricingProductsCreateSloTargetErrorComponent
                | ApiV1PricingProductsCreateTargetAvailabilityErrorComponent
                | ApiV1PricingProductsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_0 = (
                        ApiV1PricingProductsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_1 = (
                        ApiV1PricingProductsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_2 = (
                        ApiV1PricingProductsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_3 = (
                        ApiV1PricingProductsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_4 = (
                        ApiV1PricingProductsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_5 = (
                        ApiV1PricingProductsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_6 = (
                        ApiV1PricingProductsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_7 = (
                        ApiV1PricingProductsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_8 = (
                        ApiV1PricingProductsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_9 = (
                        ApiV1PricingProductsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_10 = (
                        ApiV1PricingProductsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_11 = (
                        ApiV1PricingProductsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_12 = (
                        ApiV1PricingProductsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_13 = (
                        ApiV1PricingProductsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_14 = (
                        ApiV1PricingProductsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_15 = (
                        ApiV1PricingProductsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_16 = (
                        ApiV1PricingProductsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_17 = (
                        ApiV1PricingProductsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_18 = (
                        ApiV1PricingProductsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_19 = (
                        ApiV1PricingProductsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_20 = (
                        ApiV1PricingProductsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_21 = (
                        ApiV1PricingProductsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_22 = (
                        ApiV1PricingProductsCreateBillingIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_23 = (
                        ApiV1PricingProductsCreatePricePerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_24 = (
                        ApiV1PricingProductsCreateCostPerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_25 = (
                        ApiV1PricingProductsCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_26 = (
                        ApiV1PricingProductsCreatePopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_create_error_type_27 = (
                        ApiV1PricingProductsCreateProviderTypeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_products_create_error_type_28 = (
                    ApiV1PricingProductsCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_products_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_products_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_products_create_validation_error.additional_properties = d
        return api_v1_pricing_products_create_validation_error

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
