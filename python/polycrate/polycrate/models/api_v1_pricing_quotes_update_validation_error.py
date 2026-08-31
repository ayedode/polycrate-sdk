from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quotes_update_annotations_error_component import (
        ApiV1PricingQuotesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_archived_at_error_component import (
        ApiV1PricingQuotesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_archived_error_component import (
        ApiV1PricingQuotesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_archived_reason_error_component import (
        ApiV1PricingQuotesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_criticality_error_component import (
        ApiV1PricingQuotesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_customer_email_error_component import (
        ApiV1PricingQuotesUpdateCustomerEmailErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_customer_name_error_component import (
        ApiV1PricingQuotesUpdateCustomerNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_debug_mode_error_component import (
        ApiV1PricingQuotesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_display_name_error_component import (
        ApiV1PricingQuotesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_kind_error_component import ApiV1PricingQuotesUpdateKindErrorComponent
    from ..models.api_v1_pricing_quotes_update_labels_error_component import (
        ApiV1PricingQuotesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_name_error_component import ApiV1PricingQuotesUpdateNameErrorComponent
    from ..models.api_v1_pricing_quotes_update_non_field_errors_error_component import (
        ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_platform_service_error_component import (
        ApiV1PricingQuotesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_provider_error_component import (
        ApiV1PricingQuotesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_provider_id_error_component import (
        ApiV1PricingQuotesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_provider_reference_error_component import (
        ApiV1PricingQuotesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_sla_availability_error_component import (
        ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_sla_target_error_component import (
        ApiV1PricingQuotesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_slo_availability_error_component import (
        ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_slo_target_error_component import (
        ApiV1PricingQuotesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_target_availability_error_component import (
        ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_tolerations_error_component import (
        ApiV1PricingQuotesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_total_price_error_component import (
        ApiV1PricingQuotesUpdateTotalPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_update_valid_until_error_component import (
        ApiV1PricingQuotesUpdateValidUntilErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuotesUpdateValidationError")


@_attrs_define
class ApiV1PricingQuotesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuotesUpdateAnnotationsErrorComponent |
            ApiV1PricingQuotesUpdateArchivedAtErrorComponent | ApiV1PricingQuotesUpdateArchivedErrorComponent |
            ApiV1PricingQuotesUpdateArchivedReasonErrorComponent | ApiV1PricingQuotesUpdateCriticalityErrorComponent |
            ApiV1PricingQuotesUpdateCustomerEmailErrorComponent | ApiV1PricingQuotesUpdateCustomerNameErrorComponent |
            ApiV1PricingQuotesUpdateDebugModeErrorComponent | ApiV1PricingQuotesUpdateDisplayNameErrorComponent |
            ApiV1PricingQuotesUpdateKindErrorComponent | ApiV1PricingQuotesUpdateLabelsErrorComponent |
            ApiV1PricingQuotesUpdateNameErrorComponent | ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuotesUpdatePlatformServiceErrorComponent | ApiV1PricingQuotesUpdateProviderErrorComponent |
            ApiV1PricingQuotesUpdateProviderIdErrorComponent | ApiV1PricingQuotesUpdateProviderReferenceErrorComponent |
            ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent | ApiV1PricingQuotesUpdateSlaTargetErrorComponent |
            ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent | ApiV1PricingQuotesUpdateSloTargetErrorComponent |
            ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent | ApiV1PricingQuotesUpdateTolerationsErrorComponent |
            ApiV1PricingQuotesUpdateTotalPriceErrorComponent | ApiV1PricingQuotesUpdateValidUntilErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuotesUpdateAnnotationsErrorComponent
        | ApiV1PricingQuotesUpdateArchivedAtErrorComponent
        | ApiV1PricingQuotesUpdateArchivedErrorComponent
        | ApiV1PricingQuotesUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuotesUpdateCriticalityErrorComponent
        | ApiV1PricingQuotesUpdateCustomerEmailErrorComponent
        | ApiV1PricingQuotesUpdateCustomerNameErrorComponent
        | ApiV1PricingQuotesUpdateDebugModeErrorComponent
        | ApiV1PricingQuotesUpdateDisplayNameErrorComponent
        | ApiV1PricingQuotesUpdateKindErrorComponent
        | ApiV1PricingQuotesUpdateLabelsErrorComponent
        | ApiV1PricingQuotesUpdateNameErrorComponent
        | ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuotesUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuotesUpdateProviderErrorComponent
        | ApiV1PricingQuotesUpdateProviderIdErrorComponent
        | ApiV1PricingQuotesUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuotesUpdateSlaTargetErrorComponent
        | ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuotesUpdateSloTargetErrorComponent
        | ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuotesUpdateTolerationsErrorComponent
        | ApiV1PricingQuotesUpdateTotalPriceErrorComponent
        | ApiV1PricingQuotesUpdateValidUntilErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quotes_update_annotations_error_component import (
            ApiV1PricingQuotesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_at_error_component import (
            ApiV1PricingQuotesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_error_component import (
            ApiV1PricingQuotesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_reason_error_component import (
            ApiV1PricingQuotesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_criticality_error_component import (
            ApiV1PricingQuotesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_customer_email_error_component import (
            ApiV1PricingQuotesUpdateCustomerEmailErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_customer_name_error_component import (
            ApiV1PricingQuotesUpdateCustomerNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_debug_mode_error_component import (
            ApiV1PricingQuotesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_display_name_error_component import (
            ApiV1PricingQuotesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_kind_error_component import (
            ApiV1PricingQuotesUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_labels_error_component import (
            ApiV1PricingQuotesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_name_error_component import (
            ApiV1PricingQuotesUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_non_field_errors_error_component import (
            ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_platform_service_error_component import (
            ApiV1PricingQuotesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_error_component import (
            ApiV1PricingQuotesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_id_error_component import (
            ApiV1PricingQuotesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_reference_error_component import (
            ApiV1PricingQuotesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_sla_availability_error_component import (
            ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_sla_target_error_component import (
            ApiV1PricingQuotesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_slo_availability_error_component import (
            ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_slo_target_error_component import (
            ApiV1PricingQuotesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_target_availability_error_component import (
            ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_tolerations_error_component import (
            ApiV1PricingQuotesUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_valid_until_error_component import (
            ApiV1PricingQuotesUpdateValidUntilErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateCustomerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateCustomerEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesUpdateValidUntilErrorComponent):
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
        from ..models.api_v1_pricing_quotes_update_annotations_error_component import (
            ApiV1PricingQuotesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_at_error_component import (
            ApiV1PricingQuotesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_error_component import (
            ApiV1PricingQuotesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_archived_reason_error_component import (
            ApiV1PricingQuotesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_criticality_error_component import (
            ApiV1PricingQuotesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_customer_email_error_component import (
            ApiV1PricingQuotesUpdateCustomerEmailErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_customer_name_error_component import (
            ApiV1PricingQuotesUpdateCustomerNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_debug_mode_error_component import (
            ApiV1PricingQuotesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_display_name_error_component import (
            ApiV1PricingQuotesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_kind_error_component import (
            ApiV1PricingQuotesUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_labels_error_component import (
            ApiV1PricingQuotesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_name_error_component import (
            ApiV1PricingQuotesUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_non_field_errors_error_component import (
            ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_platform_service_error_component import (
            ApiV1PricingQuotesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_error_component import (
            ApiV1PricingQuotesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_id_error_component import (
            ApiV1PricingQuotesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_provider_reference_error_component import (
            ApiV1PricingQuotesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_sla_availability_error_component import (
            ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_sla_target_error_component import (
            ApiV1PricingQuotesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_slo_availability_error_component import (
            ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_slo_target_error_component import (
            ApiV1PricingQuotesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_target_availability_error_component import (
            ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_tolerations_error_component import (
            ApiV1PricingQuotesUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_total_price_error_component import (
            ApiV1PricingQuotesUpdateTotalPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_update_valid_until_error_component import (
            ApiV1PricingQuotesUpdateValidUntilErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuotesUpdateAnnotationsErrorComponent
                | ApiV1PricingQuotesUpdateArchivedAtErrorComponent
                | ApiV1PricingQuotesUpdateArchivedErrorComponent
                | ApiV1PricingQuotesUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuotesUpdateCriticalityErrorComponent
                | ApiV1PricingQuotesUpdateCustomerEmailErrorComponent
                | ApiV1PricingQuotesUpdateCustomerNameErrorComponent
                | ApiV1PricingQuotesUpdateDebugModeErrorComponent
                | ApiV1PricingQuotesUpdateDisplayNameErrorComponent
                | ApiV1PricingQuotesUpdateKindErrorComponent
                | ApiV1PricingQuotesUpdateLabelsErrorComponent
                | ApiV1PricingQuotesUpdateNameErrorComponent
                | ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuotesUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuotesUpdateProviderErrorComponent
                | ApiV1PricingQuotesUpdateProviderIdErrorComponent
                | ApiV1PricingQuotesUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuotesUpdateSlaTargetErrorComponent
                | ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuotesUpdateSloTargetErrorComponent
                | ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuotesUpdateTolerationsErrorComponent
                | ApiV1PricingQuotesUpdateTotalPriceErrorComponent
                | ApiV1PricingQuotesUpdateValidUntilErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_0 = (
                        ApiV1PricingQuotesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_1 = (
                        ApiV1PricingQuotesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_2 = (
                        ApiV1PricingQuotesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_3 = (
                        ApiV1PricingQuotesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_4 = (
                        ApiV1PricingQuotesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_5 = (
                        ApiV1PricingQuotesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_6 = (
                        ApiV1PricingQuotesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_7 = (
                        ApiV1PricingQuotesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_8 = (
                        ApiV1PricingQuotesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_9 = (
                        ApiV1PricingQuotesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_10 = (
                        ApiV1PricingQuotesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_11 = (
                        ApiV1PricingQuotesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_12 = (
                        ApiV1PricingQuotesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_13 = (
                        ApiV1PricingQuotesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_14 = (
                        ApiV1PricingQuotesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_15 = (
                        ApiV1PricingQuotesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_16 = (
                        ApiV1PricingQuotesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_17 = (
                        ApiV1PricingQuotesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_18 = (
                        ApiV1PricingQuotesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_19 = (
                        ApiV1PricingQuotesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_20 = (
                        ApiV1PricingQuotesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_21 = (
                        ApiV1PricingQuotesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_22 = (
                        ApiV1PricingQuotesUpdateCustomerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_23 = (
                        ApiV1PricingQuotesUpdateCustomerEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_update_error_type_24 = (
                        ApiV1PricingQuotesUpdateValidUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quotes_update_error_type_25 = (
                    ApiV1PricingQuotesUpdateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quotes_update_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quotes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quotes_update_validation_error.additional_properties = d
        return api_v1_pricing_quotes_update_validation_error

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
