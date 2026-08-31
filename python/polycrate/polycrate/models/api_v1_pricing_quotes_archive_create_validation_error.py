from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quotes_archive_create_annotations_error_component import (
        ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_archived_at_error_component import (
        ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_archived_error_component import (
        ApiV1PricingQuotesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_archived_reason_error_component import (
        ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_criticality_error_component import (
        ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_customer_email_error_component import (
        ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_customer_name_error_component import (
        ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_debug_mode_error_component import (
        ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_display_name_error_component import (
        ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_kind_error_component import (
        ApiV1PricingQuotesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_labels_error_component import (
        ApiV1PricingQuotesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_name_error_component import (
        ApiV1PricingQuotesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_non_field_errors_error_component import (
        ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_platform_service_error_component import (
        ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_provider_error_component import (
        ApiV1PricingQuotesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_provider_id_error_component import (
        ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_provider_reference_error_component import (
        ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_sla_availability_error_component import (
        ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_sla_target_error_component import (
        ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_slo_availability_error_component import (
        ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_slo_target_error_component import (
        ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_target_availability_error_component import (
        ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_tolerations_error_component import (
        ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_total_price_error_component import (
        ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_archive_create_valid_until_error_component import (
        ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuotesArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingQuotesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent | ApiV1PricingQuotesArchiveCreateArchivedErrorComponent
            | ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent |
            ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent |
            ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent |
            ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent |
            ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent | ApiV1PricingQuotesArchiveCreateKindErrorComponent |
            ApiV1PricingQuotesArchiveCreateLabelsErrorComponent | ApiV1PricingQuotesArchiveCreateNameErrorComponent |
            ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingQuotesArchiveCreateProviderErrorComponent | ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent
            | ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent |
            ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent |
            ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent |
            ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingQuotesArchiveCreateArchivedErrorComponent
        | ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent
        | ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent
        | ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent
        | ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent
        | ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingQuotesArchiveCreateKindErrorComponent
        | ApiV1PricingQuotesArchiveCreateLabelsErrorComponent
        | ApiV1PricingQuotesArchiveCreateNameErrorComponent
        | ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingQuotesArchiveCreateProviderErrorComponent
        | ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent
        | ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent
        | ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent
        | ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent
        | ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quotes_archive_create_annotations_error_component import (
            ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_at_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_reason_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_criticality_error_component import (
            ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_customer_email_error_component import (
            ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_customer_name_error_component import (
            ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_debug_mode_error_component import (
            ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_display_name_error_component import (
            ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_kind_error_component import (
            ApiV1PricingQuotesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_labels_error_component import (
            ApiV1PricingQuotesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_name_error_component import (
            ApiV1PricingQuotesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_platform_service_error_component import (
            ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_id_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_reference_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_sla_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_sla_target_error_component import (
            ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_slo_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_slo_target_error_component import (
            ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_target_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_tolerations_error_component import (
            ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_valid_until_error_component import (
            ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent):
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
        from ..models.api_v1_pricing_quotes_archive_create_annotations_error_component import (
            ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_at_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_archived_reason_error_component import (
            ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_criticality_error_component import (
            ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_customer_email_error_component import (
            ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_customer_name_error_component import (
            ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_debug_mode_error_component import (
            ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_display_name_error_component import (
            ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_kind_error_component import (
            ApiV1PricingQuotesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_labels_error_component import (
            ApiV1PricingQuotesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_name_error_component import (
            ApiV1PricingQuotesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_platform_service_error_component import (
            ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_id_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_provider_reference_error_component import (
            ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_sla_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_sla_target_error_component import (
            ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_slo_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_slo_target_error_component import (
            ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_target_availability_error_component import (
            ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_tolerations_error_component import (
            ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_total_price_error_component import (
            ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quotes_archive_create_valid_until_error_component import (
            ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingQuotesArchiveCreateArchivedErrorComponent
                | ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent
                | ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent
                | ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent
                | ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent
                | ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingQuotesArchiveCreateKindErrorComponent
                | ApiV1PricingQuotesArchiveCreateLabelsErrorComponent
                | ApiV1PricingQuotesArchiveCreateNameErrorComponent
                | ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingQuotesArchiveCreateProviderErrorComponent
                | ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent
                | ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent
                | ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent
                | ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent
                | ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_0 = (
                        ApiV1PricingQuotesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_1 = (
                        ApiV1PricingQuotesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_2 = (
                        ApiV1PricingQuotesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_3 = (
                        ApiV1PricingQuotesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_4 = (
                        ApiV1PricingQuotesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_5 = (
                        ApiV1PricingQuotesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_6 = (
                        ApiV1PricingQuotesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_7 = (
                        ApiV1PricingQuotesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_8 = (
                        ApiV1PricingQuotesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_9 = (
                        ApiV1PricingQuotesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_10 = (
                        ApiV1PricingQuotesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_11 = (
                        ApiV1PricingQuotesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_12 = (
                        ApiV1PricingQuotesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_13 = (
                        ApiV1PricingQuotesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_14 = (
                        ApiV1PricingQuotesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_15 = (
                        ApiV1PricingQuotesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_16 = (
                        ApiV1PricingQuotesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_17 = (
                        ApiV1PricingQuotesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_18 = (
                        ApiV1PricingQuotesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_19 = (
                        ApiV1PricingQuotesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_20 = (
                        ApiV1PricingQuotesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_21 = (
                        ApiV1PricingQuotesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_22 = (
                        ApiV1PricingQuotesArchiveCreateCustomerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_23 = (
                        ApiV1PricingQuotesArchiveCreateCustomerEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_archive_create_error_type_24 = (
                        ApiV1PricingQuotesArchiveCreateValidUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quotes_archive_create_error_type_25 = (
                    ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quotes_archive_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quotes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quotes_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_quotes_archive_create_validation_error

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
