from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_archive_create_access_count_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_annotations_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_archived_at_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_archived_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_archived_reason_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_booking_id_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_configuration_json_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_criticality_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_debug_mode_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_display_name_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_kind_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_labels_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_last_access_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_name_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_non_field_errors_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_platform_service_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_provider_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_provider_id_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_provider_reference_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_sla_availability_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_sla_target_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_slo_availability_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_slo_target_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_target_availability_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_tolerations_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_archive_create_total_price_error_component import (
        ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent |
            ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent
        | ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_archive_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_kind_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_labels_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_name_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_archive_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_booking_id_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_kind_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_labels_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_name_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_calculator_states_archive_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent
                | ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_0 = (
                        ApiV1PricingCalculatorStatesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_1 = (
                        ApiV1PricingCalculatorStatesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_2 = (
                        ApiV1PricingCalculatorStatesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_3 = (
                        ApiV1PricingCalculatorStatesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_4 = (
                        ApiV1PricingCalculatorStatesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_5 = (
                        ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_6 = (
                        ApiV1PricingCalculatorStatesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_7 = (
                        ApiV1PricingCalculatorStatesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_8 = (
                        ApiV1PricingCalculatorStatesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_9 = (
                        ApiV1PricingCalculatorStatesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_10 = (
                        ApiV1PricingCalculatorStatesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_11 = (
                        ApiV1PricingCalculatorStatesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_12 = (
                        ApiV1PricingCalculatorStatesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_13 = (
                        ApiV1PricingCalculatorStatesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_14 = (
                        ApiV1PricingCalculatorStatesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_15 = (
                        ApiV1PricingCalculatorStatesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_16 = (
                        ApiV1PricingCalculatorStatesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_17 = (
                        ApiV1PricingCalculatorStatesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_18 = (
                        ApiV1PricingCalculatorStatesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_19 = (
                        ApiV1PricingCalculatorStatesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_20 = (
                        ApiV1PricingCalculatorStatesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_21 = (
                        ApiV1PricingCalculatorStatesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_22 = (
                        ApiV1PricingCalculatorStatesArchiveCreateConfigurationJsonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_23 = (
                        ApiV1PricingCalculatorStatesArchiveCreateTotalPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_24 = (
                        ApiV1PricingCalculatorStatesArchiveCreateLastAccessErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_25 = (
                        ApiV1PricingCalculatorStatesArchiveCreateAccessCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_26 = (
                    ApiV1PricingCalculatorStatesArchiveCreateBookingIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_archive_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_archive_create_validation_error

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
