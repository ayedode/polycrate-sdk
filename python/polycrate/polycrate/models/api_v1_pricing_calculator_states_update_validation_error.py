from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_update_access_count_error_component import (
        ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_annotations_error_component import (
        ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_archived_at_error_component import (
        ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_archived_error_component import (
        ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_archived_reason_error_component import (
        ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_booking_id_error_component import (
        ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_configuration_json_error_component import (
        ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_criticality_error_component import (
        ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_debug_mode_error_component import (
        ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_display_name_error_component import (
        ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_kind_error_component import (
        ApiV1PricingCalculatorStatesUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_labels_error_component import (
        ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_last_access_error_component import (
        ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_name_error_component import (
        ApiV1PricingCalculatorStatesUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_non_field_errors_error_component import (
        ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_platform_service_error_component import (
        ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_provider_error_component import (
        ApiV1PricingCalculatorStatesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_provider_id_error_component import (
        ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_provider_reference_error_component import (
        ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_reconciliation_enabled_error_component import (
        ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_sla_availability_error_component import (
        ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_sla_target_error_component import (
        ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_slo_availability_error_component import (
        ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_slo_target_error_component import (
        ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_target_availability_error_component import (
        ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_tolerations_error_component import (
        ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_update_total_price_error_component import (
        ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesUpdateValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent |
            ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent |
            ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent |
            ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent |
            ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent |
            ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent |
            ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent |
            ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent |
            ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent |
            ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent |
            ApiV1PricingCalculatorStatesUpdateKindErrorComponent | ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent |
            ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent |
            ApiV1PricingCalculatorStatesUpdateNameErrorComponent |
            ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent |
            ApiV1PricingCalculatorStatesUpdateProviderErrorComponent |
            ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent |
            ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent |
            ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent |
            ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent |
            ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent |
            ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent
        | ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent
        | ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent
        | ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent
        | ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent
        | ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent
        | ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent
        | ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent
        | ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent
        | ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent
        | ApiV1PricingCalculatorStatesUpdateKindErrorComponent
        | ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent
        | ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent
        | ApiV1PricingCalculatorStatesUpdateNameErrorComponent
        | ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent
        | ApiV1PricingCalculatorStatesUpdateProviderErrorComponent
        | ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent
        | ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent
        | ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent
        | ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent
        | ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent
        | ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_update_access_count_error_component import (
            ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_annotations_error_component import (
            ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_at_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_criticality_error_component import (
            ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_display_name_error_component import (
            ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_kind_error_component import (
            ApiV1PricingCalculatorStatesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_labels_error_component import (
            ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_last_access_error_component import (
            ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_name_error_component import (
            ApiV1PricingCalculatorStatesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_platform_service_error_component import (
            ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_id_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_sla_target_error_component import (
            ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_slo_target_error_component import (
            ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_target_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_tolerations_error_component import (
            ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_total_price_error_component import (
            ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_update_access_count_error_component import (
            ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_annotations_error_component import (
            ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_at_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_booking_id_error_component import (
            ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_criticality_error_component import (
            ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_display_name_error_component import (
            ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_kind_error_component import (
            ApiV1PricingCalculatorStatesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_labels_error_component import (
            ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_last_access_error_component import (
            ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_name_error_component import (
            ApiV1PricingCalculatorStatesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_platform_service_error_component import (
            ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_id_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_sla_target_error_component import (
            ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_slo_target_error_component import (
            ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_target_availability_error_component import (
            ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_tolerations_error_component import (
            ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_update_total_price_error_component import (
            ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent
                | ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent
                | ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent
                | ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent
                | ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent
                | ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent
                | ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent
                | ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent
                | ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent
                | ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent
                | ApiV1PricingCalculatorStatesUpdateKindErrorComponent
                | ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent
                | ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent
                | ApiV1PricingCalculatorStatesUpdateNameErrorComponent
                | ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent
                | ApiV1PricingCalculatorStatesUpdateProviderErrorComponent
                | ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent
                | ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent
                | ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent
                | ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent
                | ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent
                | ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_0 = (
                        ApiV1PricingCalculatorStatesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_1 = (
                        ApiV1PricingCalculatorStatesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_2 = (
                        ApiV1PricingCalculatorStatesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_3 = (
                        ApiV1PricingCalculatorStatesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_4 = (
                        ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_5 = (
                        ApiV1PricingCalculatorStatesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_6 = (
                        ApiV1PricingCalculatorStatesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_7 = (
                        ApiV1PricingCalculatorStatesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_8 = (
                        ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_9 = (
                        ApiV1PricingCalculatorStatesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_10 = (
                        ApiV1PricingCalculatorStatesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_11 = (
                        ApiV1PricingCalculatorStatesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_12 = (
                        ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_13 = (
                        ApiV1PricingCalculatorStatesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_14 = (
                        ApiV1PricingCalculatorStatesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_15 = (
                        ApiV1PricingCalculatorStatesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_16 = (
                        ApiV1PricingCalculatorStatesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_17 = (
                        ApiV1PricingCalculatorStatesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_18 = (
                        ApiV1PricingCalculatorStatesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_19 = (
                        ApiV1PricingCalculatorStatesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_20 = (
                        ApiV1PricingCalculatorStatesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_21 = (
                        ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_22 = (
                        ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_23 = (
                        ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_24 = (
                        ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_update_error_type_25 = (
                        ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_update_error_type_26 = (
                    ApiV1PricingCalculatorStatesUpdateBookingIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_update_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_update_validation_error

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
