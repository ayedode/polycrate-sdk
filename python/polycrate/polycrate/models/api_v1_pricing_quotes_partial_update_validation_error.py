from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quotes_partial_update_annotations_error_component import (
        ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_archived_at_error_component import (
        ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_archived_error_component import (
        ApiV1PricingQuotesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_archived_reason_error_component import (
        ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_criticality_error_component import (
        ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_customer_email_error_component import (
        ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_customer_name_error_component import (
        ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_debug_mode_error_component import (
        ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_display_name_error_component import (
        ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_kind_error_component import (
        ApiV1PricingQuotesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_labels_error_component import (
        ApiV1PricingQuotesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_name_error_component import (
        ApiV1PricingQuotesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_non_field_errors_error_component import (
        ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_platform_service_error_component import (
        ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_provider_error_component import (
        ApiV1PricingQuotesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_provider_id_error_component import (
        ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_provider_reference_error_component import (
        ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_sla_availability_error_component import (
        ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_sla_target_error_component import (
        ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_slo_availability_error_component import (
        ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_slo_target_error_component import (
        ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_target_availability_error_component import (
        ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_tolerations_error_component import (
        ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_total_price_error_component import (
        ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_partial_update_valid_until_error_component import (
        ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuotesPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingQuotesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent | ApiV1PricingQuotesPartialUpdateArchivedErrorComponent
            | ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent |
            ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent |
            ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent |
            ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent |
            ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent | ApiV1PricingQuotesPartialUpdateKindErrorComponent |
            ApiV1PricingQuotesPartialUpdateLabelsErrorComponent | ApiV1PricingQuotesPartialUpdateNameErrorComponent |
            ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingQuotesPartialUpdateProviderErrorComponent | ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent
            | ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent |
            ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent |
            ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent |
            ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingQuotesPartialUpdateArchivedErrorComponent
        | ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent
        | ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent
        | ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent
        | ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent
        | ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingQuotesPartialUpdateKindErrorComponent
        | ApiV1PricingQuotesPartialUpdateLabelsErrorComponent
        | ApiV1PricingQuotesPartialUpdateNameErrorComponent
        | ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuotesPartialUpdateProviderErrorComponent
        | ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent
        | ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent
        | ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent
        | ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent
        | ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quotes_partial_update_annotations_error_component import (
            ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_at_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_reason_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_criticality_error_component import (
            ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_customer_email_error_component import (
            ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_customer_name_error_component import (
            ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_debug_mode_error_component import (
            ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_display_name_error_component import (
            ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_kind_error_component import (
            ApiV1PricingQuotesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_labels_error_component import (
            ApiV1PricingQuotesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_name_error_component import (
            ApiV1PricingQuotesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_platform_service_error_component import (
            ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_id_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_reference_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_sla_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_sla_target_error_component import (
            ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_slo_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_slo_target_error_component import (
            ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_target_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_tolerations_error_component import (
            ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_valid_until_error_component import (
            ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent):
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
        from ..models.api_v1_pricing_quotes_partial_update_annotations_error_component import (
            ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_at_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_archived_reason_error_component import (
            ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_criticality_error_component import (
            ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_customer_email_error_component import (
            ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_customer_name_error_component import (
            ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_debug_mode_error_component import (
            ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_display_name_error_component import (
            ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_kind_error_component import (
            ApiV1PricingQuotesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_labels_error_component import (
            ApiV1PricingQuotesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_name_error_component import (
            ApiV1PricingQuotesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_platform_service_error_component import (
            ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_id_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_provider_reference_error_component import (
            ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_sla_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_sla_target_error_component import (
            ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_slo_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_slo_target_error_component import (
            ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_target_availability_error_component import (
            ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_tolerations_error_component import (
            ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_total_price_error_component import (
            ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_partial_update_valid_until_error_component import (
            ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingQuotesPartialUpdateArchivedErrorComponent
                | ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent
                | ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent
                | ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent
                | ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent
                | ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingQuotesPartialUpdateKindErrorComponent
                | ApiV1PricingQuotesPartialUpdateLabelsErrorComponent
                | ApiV1PricingQuotesPartialUpdateNameErrorComponent
                | ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuotesPartialUpdateProviderErrorComponent
                | ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent
                | ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent
                | ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent
                | ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent
                | ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_0 = (
                        ApiV1PricingQuotesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_1 = (
                        ApiV1PricingQuotesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_2 = (
                        ApiV1PricingQuotesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_3 = (
                        ApiV1PricingQuotesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_4 = (
                        ApiV1PricingQuotesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_5 = (
                        ApiV1PricingQuotesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_6 = (
                        ApiV1PricingQuotesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_7 = (
                        ApiV1PricingQuotesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_8 = (
                        ApiV1PricingQuotesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_9 = (
                        ApiV1PricingQuotesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_10 = (
                        ApiV1PricingQuotesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_11 = (
                        ApiV1PricingQuotesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_12 = (
                        ApiV1PricingQuotesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_13 = (
                        ApiV1PricingQuotesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_14 = (
                        ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_15 = (
                        ApiV1PricingQuotesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_16 = (
                        ApiV1PricingQuotesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_17 = (
                        ApiV1PricingQuotesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_18 = (
                        ApiV1PricingQuotesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_19 = (
                        ApiV1PricingQuotesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_20 = (
                        ApiV1PricingQuotesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_21 = (
                        ApiV1PricingQuotesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_22 = (
                        ApiV1PricingQuotesPartialUpdateCustomerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_23 = (
                        ApiV1PricingQuotesPartialUpdateCustomerEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_partial_update_error_type_24 = (
                        ApiV1PricingQuotesPartialUpdateValidUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quotes_partial_update_error_type_25 = (
                    ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quotes_partial_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quotes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quotes_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_quotes_partial_update_validation_error

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
