from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_products_partial_update_annotations_error_component import (
        ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_archived_at_error_component import (
        ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_archived_error_component import (
        ApiV1PricingProductsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_archived_reason_error_component import (
        ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_billing_interval_error_component import (
        ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_config_error_component import (
        ApiV1PricingProductsPartialUpdateConfigErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_cost_per_unit_error_component import (
        ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_criticality_error_component import (
        ApiV1PricingProductsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_debug_mode_error_component import (
        ApiV1PricingProductsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_display_name_error_component import (
        ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_kind_error_component import (
        ApiV1PricingProductsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_labels_error_component import (
        ApiV1PricingProductsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_name_error_component import (
        ApiV1PricingProductsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_non_field_errors_error_component import (
        ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_platform_service_error_component import (
        ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_pop_error_component import (
        ApiV1PricingProductsPartialUpdatePopErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_price_per_unit_error_component import (
        ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_provider_entity_error_component import (
        ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_provider_error_component import (
        ApiV1PricingProductsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_provider_id_error_component import (
        ApiV1PricingProductsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_provider_reference_error_component import (
        ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_provider_type_id_error_component import (
        ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_sla_availability_error_component import (
        ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_sla_target_error_component import (
        ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_slo_availability_error_component import (
        ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_slo_target_error_component import (
        ApiV1PricingProductsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_target_availability_error_component import (
        ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_partial_update_tolerations_error_component import (
        ApiV1PricingProductsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingProductsPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingProductsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingProductsPartialUpdateArchivedErrorComponent |
            ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent |
            ApiV1PricingProductsPartialUpdateConfigErrorComponent |
            ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent |
            ApiV1PricingProductsPartialUpdateCriticalityErrorComponent |
            ApiV1PricingProductsPartialUpdateDebugModeErrorComponent |
            ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent | ApiV1PricingProductsPartialUpdateKindErrorComponent
            | ApiV1PricingProductsPartialUpdateLabelsErrorComponent | ApiV1PricingProductsPartialUpdateNameErrorComponent |
            ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingProductsPartialUpdatePopErrorComponent | ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent
            | ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent |
            ApiV1PricingProductsPartialUpdateProviderErrorComponent |
            ApiV1PricingProductsPartialUpdateProviderIdErrorComponent |
            ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent |
            ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingProductsPartialUpdateSloTargetErrorComponent |
            ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingProductsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingProductsPartialUpdateArchivedErrorComponent
        | ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent
        | ApiV1PricingProductsPartialUpdateConfigErrorComponent
        | ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent
        | ApiV1PricingProductsPartialUpdateCriticalityErrorComponent
        | ApiV1PricingProductsPartialUpdateDebugModeErrorComponent
        | ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingProductsPartialUpdateKindErrorComponent
        | ApiV1PricingProductsPartialUpdateLabelsErrorComponent
        | ApiV1PricingProductsPartialUpdateNameErrorComponent
        | ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingProductsPartialUpdatePopErrorComponent
        | ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent
        | ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent
        | ApiV1PricingProductsPartialUpdateProviderErrorComponent
        | ApiV1PricingProductsPartialUpdateProviderIdErrorComponent
        | ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent
        | ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingProductsPartialUpdateSloTargetErrorComponent
        | ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingProductsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_products_partial_update_annotations_error_component import (
            ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_at_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_reason_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_billing_interval_error_component import (
            ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_cost_per_unit_error_component import (
            ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_criticality_error_component import (
            ApiV1PricingProductsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_debug_mode_error_component import (
            ApiV1PricingProductsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_display_name_error_component import (
            ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_kind_error_component import (
            ApiV1PricingProductsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_labels_error_component import (
            ApiV1PricingProductsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_name_error_component import (
            ApiV1PricingProductsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_non_field_errors_error_component import (
            ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_platform_service_error_component import (
            ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_pop_error_component import (
            ApiV1PricingProductsPartialUpdatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_price_per_unit_error_component import (
            ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_entity_error_component import (
            ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_error_component import (
            ApiV1PricingProductsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_id_error_component import (
            ApiV1PricingProductsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_reference_error_component import (
            ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_type_id_error_component import (
            ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_sla_availability_error_component import (
            ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_sla_target_error_component import (
            ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_slo_availability_error_component import (
            ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_slo_target_error_component import (
            ApiV1PricingProductsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_target_availability_error_component import (
            ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_tolerations_error_component import (
            ApiV1PricingProductsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdatePopErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent):
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
        from ..models.api_v1_pricing_products_partial_update_annotations_error_component import (
            ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_at_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_archived_reason_error_component import (
            ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_billing_interval_error_component import (
            ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_config_error_component import (
            ApiV1PricingProductsPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_cost_per_unit_error_component import (
            ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_criticality_error_component import (
            ApiV1PricingProductsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_debug_mode_error_component import (
            ApiV1PricingProductsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_display_name_error_component import (
            ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_kind_error_component import (
            ApiV1PricingProductsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_labels_error_component import (
            ApiV1PricingProductsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_name_error_component import (
            ApiV1PricingProductsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_non_field_errors_error_component import (
            ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_platform_service_error_component import (
            ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_pop_error_component import (
            ApiV1PricingProductsPartialUpdatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_price_per_unit_error_component import (
            ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_entity_error_component import (
            ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_error_component import (
            ApiV1PricingProductsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_id_error_component import (
            ApiV1PricingProductsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_reference_error_component import (
            ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_provider_type_id_error_component import (
            ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_sla_availability_error_component import (
            ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_sla_target_error_component import (
            ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_slo_availability_error_component import (
            ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_slo_target_error_component import (
            ApiV1PricingProductsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_target_availability_error_component import (
            ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_partial_update_tolerations_error_component import (
            ApiV1PricingProductsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingProductsPartialUpdateArchivedErrorComponent
                | ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent
                | ApiV1PricingProductsPartialUpdateConfigErrorComponent
                | ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent
                | ApiV1PricingProductsPartialUpdateCriticalityErrorComponent
                | ApiV1PricingProductsPartialUpdateDebugModeErrorComponent
                | ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingProductsPartialUpdateKindErrorComponent
                | ApiV1PricingProductsPartialUpdateLabelsErrorComponent
                | ApiV1PricingProductsPartialUpdateNameErrorComponent
                | ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingProductsPartialUpdatePopErrorComponent
                | ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent
                | ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent
                | ApiV1PricingProductsPartialUpdateProviderErrorComponent
                | ApiV1PricingProductsPartialUpdateProviderIdErrorComponent
                | ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent
                | ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingProductsPartialUpdateSloTargetErrorComponent
                | ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingProductsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_0 = (
                        ApiV1PricingProductsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_1 = (
                        ApiV1PricingProductsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_2 = (
                        ApiV1PricingProductsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_3 = (
                        ApiV1PricingProductsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_4 = (
                        ApiV1PricingProductsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_5 = (
                        ApiV1PricingProductsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_6 = (
                        ApiV1PricingProductsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_7 = (
                        ApiV1PricingProductsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_8 = (
                        ApiV1PricingProductsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_9 = (
                        ApiV1PricingProductsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_10 = (
                        ApiV1PricingProductsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_11 = (
                        ApiV1PricingProductsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_12 = (
                        ApiV1PricingProductsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_13 = (
                        ApiV1PricingProductsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_14 = (
                        ApiV1PricingProductsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_15 = (
                        ApiV1PricingProductsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_16 = (
                        ApiV1PricingProductsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_17 = (
                        ApiV1PricingProductsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_18 = (
                        ApiV1PricingProductsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_19 = (
                        ApiV1PricingProductsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_20 = (
                        ApiV1PricingProductsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_21 = (
                        ApiV1PricingProductsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_22 = (
                        ApiV1PricingProductsPartialUpdateBillingIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_23 = (
                        ApiV1PricingProductsPartialUpdatePricePerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_24 = (
                        ApiV1PricingProductsPartialUpdateCostPerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_25 = (
                        ApiV1PricingProductsPartialUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_26 = (
                        ApiV1PricingProductsPartialUpdatePopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_partial_update_error_type_27 = (
                        ApiV1PricingProductsPartialUpdateProviderTypeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_products_partial_update_error_type_28 = (
                    ApiV1PricingProductsPartialUpdateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_products_partial_update_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_products_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_products_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_products_partial_update_validation_error

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
