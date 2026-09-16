from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_partial_update_access_count_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_annotations_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_archived_at_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_archived_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_archived_reason_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_booking_id_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_configuration_json_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_criticality_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_debug_mode_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_display_name_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_kind_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_labels_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_last_access_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_name_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_non_field_errors_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_platform_service_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_provider_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_provider_id_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_provider_reference_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_sla_availability_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_sla_target_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_slo_availability_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_slo_target_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_target_availability_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_tolerations_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_partial_update_total_price_error_component import (
        ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent |
            ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent
        | ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_partial_update_access_count_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_annotations_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_at_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_criticality_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_display_name_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_kind_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_labels_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_last_access_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_name_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_platform_service_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_id_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_sla_target_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_slo_target_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_target_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_tolerations_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_total_price_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_partial_update_access_count_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_annotations_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_at_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_booking_id_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_criticality_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_display_name_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_kind_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_labels_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_last_access_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_name_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_platform_service_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_id_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_sla_target_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_slo_target_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_target_availability_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_tolerations_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_partial_update_total_price_error_component import (
            ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent
                | ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_0 = (
                        ApiV1PricingCalculatorStatesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_1 = (
                        ApiV1PricingCalculatorStatesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_2 = (
                        ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_3 = (
                        ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_4 = (
                        ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_5 = (
                        ApiV1PricingCalculatorStatesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_6 = (
                        ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_7 = (
                        ApiV1PricingCalculatorStatesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_8 = (
                        ApiV1PricingCalculatorStatesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_9 = (
                        ApiV1PricingCalculatorStatesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_10 = (
                        ApiV1PricingCalculatorStatesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_11 = (
                        ApiV1PricingCalculatorStatesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_12 = (
                        ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_13 = (
                        ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_14 = (
                        ApiV1PricingCalculatorStatesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_15 = (
                        ApiV1PricingCalculatorStatesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_16 = (
                        ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_17 = (
                        ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_18 = (
                        ApiV1PricingCalculatorStatesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_19 = (
                        ApiV1PricingCalculatorStatesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_20 = (
                        ApiV1PricingCalculatorStatesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_21 = (
                        ApiV1PricingCalculatorStatesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_22 = (
                        ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_23 = (
                        ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_24 = (
                        ApiV1PricingCalculatorStatesPartialUpdateLastAccessErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_25 = (
                        ApiV1PricingCalculatorStatesPartialUpdateAccessCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_26 = (
                    ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_partial_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_partial_update_validation_error

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
