from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_create_access_count_error_component import (
        ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_annotations_error_component import (
        ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_archived_at_error_component import (
        ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_archived_error_component import (
        ApiV1PricingCalculatorStatesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_archived_reason_error_component import (
        ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_booking_id_error_component import (
        ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_configuration_json_error_component import (
        ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_criticality_error_component import (
        ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_debug_mode_error_component import (
        ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_display_name_error_component import (
        ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_kind_error_component import (
        ApiV1PricingCalculatorStatesCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_labels_error_component import (
        ApiV1PricingCalculatorStatesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_last_access_error_component import (
        ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_name_error_component import (
        ApiV1PricingCalculatorStatesCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_non_field_errors_error_component import (
        ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_platform_service_error_component import (
        ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_provider_error_component import (
        ApiV1PricingCalculatorStatesCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_provider_id_error_component import (
        ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_provider_reference_error_component import (
        ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_reconciliation_enabled_error_component import (
        ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_sla_availability_error_component import (
        ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_sla_target_error_component import (
        ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_slo_availability_error_component import (
        ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_slo_target_error_component import (
        ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_target_availability_error_component import (
        ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_tolerations_error_component import (
        ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_create_total_price_error_component import (
        ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesCreateValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent |
            ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent |
            ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent |
            ApiV1PricingCalculatorStatesCreateArchivedErrorComponent |
            ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent |
            ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent |
            ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent |
            ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent |
            ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent |
            ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent |
            ApiV1PricingCalculatorStatesCreateKindErrorComponent | ApiV1PricingCalculatorStatesCreateLabelsErrorComponent |
            ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent |
            ApiV1PricingCalculatorStatesCreateNameErrorComponent |
            ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent |
            ApiV1PricingCalculatorStatesCreateProviderErrorComponent |
            ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent |
            ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent |
            ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent |
            ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent |
            ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent |
            ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent
        | ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent
        | ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent
        | ApiV1PricingCalculatorStatesCreateArchivedErrorComponent
        | ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent
        | ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent
        | ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent
        | ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent
        | ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent
        | ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent
        | ApiV1PricingCalculatorStatesCreateKindErrorComponent
        | ApiV1PricingCalculatorStatesCreateLabelsErrorComponent
        | ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent
        | ApiV1PricingCalculatorStatesCreateNameErrorComponent
        | ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent
        | ApiV1PricingCalculatorStatesCreateProviderErrorComponent
        | ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent
        | ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent
        | ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent
        | ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent
        | ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent
        | ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_kind_error_component import (
            ApiV1PricingCalculatorStatesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_labels_error_component import (
            ApiV1PricingCalculatorStatesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_name_error_component import (
            ApiV1PricingCalculatorStatesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_booking_id_error_component import (
            ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_kind_error_component import (
            ApiV1PricingCalculatorStatesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_labels_error_component import (
            ApiV1PricingCalculatorStatesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_name_error_component import (
            ApiV1PricingCalculatorStatesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent
                | ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent
                | ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent
                | ApiV1PricingCalculatorStatesCreateArchivedErrorComponent
                | ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent
                | ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent
                | ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent
                | ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent
                | ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent
                | ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent
                | ApiV1PricingCalculatorStatesCreateKindErrorComponent
                | ApiV1PricingCalculatorStatesCreateLabelsErrorComponent
                | ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent
                | ApiV1PricingCalculatorStatesCreateNameErrorComponent
                | ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent
                | ApiV1PricingCalculatorStatesCreateProviderErrorComponent
                | ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent
                | ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent
                | ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent
                | ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent
                | ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent
                | ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_0 = (
                        ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_1 = (
                        ApiV1PricingCalculatorStatesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_2 = (
                        ApiV1PricingCalculatorStatesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_3 = (
                        ApiV1PricingCalculatorStatesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_4 = (
                        ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_5 = (
                        ApiV1PricingCalculatorStatesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_6 = (
                        ApiV1PricingCalculatorStatesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_7 = (
                        ApiV1PricingCalculatorStatesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_8 = (
                        ApiV1PricingCalculatorStatesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_9 = (
                        ApiV1PricingCalculatorStatesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_10 = (
                        ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_11 = (
                        ApiV1PricingCalculatorStatesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_12 = (
                        ApiV1PricingCalculatorStatesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_13 = (
                        ApiV1PricingCalculatorStatesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_14 = (
                        ApiV1PricingCalculatorStatesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_15 = (
                        ApiV1PricingCalculatorStatesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_16 = (
                        ApiV1PricingCalculatorStatesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_17 = (
                        ApiV1PricingCalculatorStatesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_18 = (
                        ApiV1PricingCalculatorStatesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_19 = (
                        ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_20 = (
                        ApiV1PricingCalculatorStatesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_21 = (
                        ApiV1PricingCalculatorStatesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_22 = (
                        ApiV1PricingCalculatorStatesCreateConfigurationJsonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_23 = (
                        ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_24 = (
                        ApiV1PricingCalculatorStatesCreateLastAccessErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_create_error_type_25 = (
                        ApiV1PricingCalculatorStatesCreateAccessCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_create_error_type_26 = (
                    ApiV1PricingCalculatorStatesCreateBookingIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_create_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_create_validation_error

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
