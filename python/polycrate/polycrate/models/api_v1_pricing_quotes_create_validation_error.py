from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quotes_create_annotations_error_component import (
        ApiV1PricingQuotesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_archived_at_error_component import (
        ApiV1PricingQuotesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_archived_error_component import (
        ApiV1PricingQuotesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_archived_reason_error_component import (
        ApiV1PricingQuotesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_criticality_error_component import (
        ApiV1PricingQuotesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_customer_email_error_component import (
        ApiV1PricingQuotesCreateCustomerEmailErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_customer_name_error_component import (
        ApiV1PricingQuotesCreateCustomerNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_debug_mode_error_component import (
        ApiV1PricingQuotesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_display_name_error_component import (
        ApiV1PricingQuotesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_kind_error_component import ApiV1PricingQuotesCreateKindErrorComponent
    from ..models.api_v1_pricing_quotes_create_labels_error_component import (
        ApiV1PricingQuotesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_name_error_component import ApiV1PricingQuotesCreateNameErrorComponent
    from ..models.api_v1_pricing_quotes_create_non_field_errors_error_component import (
        ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_platform_service_error_component import (
        ApiV1PricingQuotesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_provider_error_component import (
        ApiV1PricingQuotesCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_provider_id_error_component import (
        ApiV1PricingQuotesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_provider_reference_error_component import (
        ApiV1PricingQuotesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_sla_availability_error_component import (
        ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_sla_target_error_component import (
        ApiV1PricingQuotesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_slo_availability_error_component import (
        ApiV1PricingQuotesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_slo_target_error_component import (
        ApiV1PricingQuotesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_target_availability_error_component import (
        ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_tolerations_error_component import (
        ApiV1PricingQuotesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_total_price_error_component import (
        ApiV1PricingQuotesCreateTotalPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quotes_create_valid_until_error_component import (
        ApiV1PricingQuotesCreateValidUntilErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuotesCreateValidationError")


@_attrs_define
class ApiV1PricingQuotesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuotesCreateAnnotationsErrorComponent |
            ApiV1PricingQuotesCreateArchivedAtErrorComponent | ApiV1PricingQuotesCreateArchivedErrorComponent |
            ApiV1PricingQuotesCreateArchivedReasonErrorComponent | ApiV1PricingQuotesCreateCriticalityErrorComponent |
            ApiV1PricingQuotesCreateCustomerEmailErrorComponent | ApiV1PricingQuotesCreateCustomerNameErrorComponent |
            ApiV1PricingQuotesCreateDebugModeErrorComponent | ApiV1PricingQuotesCreateDisplayNameErrorComponent |
            ApiV1PricingQuotesCreateKindErrorComponent | ApiV1PricingQuotesCreateLabelsErrorComponent |
            ApiV1PricingQuotesCreateNameErrorComponent | ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuotesCreatePlatformServiceErrorComponent | ApiV1PricingQuotesCreateProviderErrorComponent |
            ApiV1PricingQuotesCreateProviderIdErrorComponent | ApiV1PricingQuotesCreateProviderReferenceErrorComponent |
            ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent | ApiV1PricingQuotesCreateSlaTargetErrorComponent |
            ApiV1PricingQuotesCreateSloAvailabilityErrorComponent | ApiV1PricingQuotesCreateSloTargetErrorComponent |
            ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent | ApiV1PricingQuotesCreateTolerationsErrorComponent |
            ApiV1PricingQuotesCreateTotalPriceErrorComponent | ApiV1PricingQuotesCreateValidUntilErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuotesCreateAnnotationsErrorComponent
        | ApiV1PricingQuotesCreateArchivedAtErrorComponent
        | ApiV1PricingQuotesCreateArchivedErrorComponent
        | ApiV1PricingQuotesCreateArchivedReasonErrorComponent
        | ApiV1PricingQuotesCreateCriticalityErrorComponent
        | ApiV1PricingQuotesCreateCustomerEmailErrorComponent
        | ApiV1PricingQuotesCreateCustomerNameErrorComponent
        | ApiV1PricingQuotesCreateDebugModeErrorComponent
        | ApiV1PricingQuotesCreateDisplayNameErrorComponent
        | ApiV1PricingQuotesCreateKindErrorComponent
        | ApiV1PricingQuotesCreateLabelsErrorComponent
        | ApiV1PricingQuotesCreateNameErrorComponent
        | ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuotesCreatePlatformServiceErrorComponent
        | ApiV1PricingQuotesCreateProviderErrorComponent
        | ApiV1PricingQuotesCreateProviderIdErrorComponent
        | ApiV1PricingQuotesCreateProviderReferenceErrorComponent
        | ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuotesCreateSlaTargetErrorComponent
        | ApiV1PricingQuotesCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuotesCreateSloTargetErrorComponent
        | ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuotesCreateTolerationsErrorComponent
        | ApiV1PricingQuotesCreateTotalPriceErrorComponent
        | ApiV1PricingQuotesCreateValidUntilErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quotes_create_annotations_error_component import (
            ApiV1PricingQuotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_at_error_component import (
            ApiV1PricingQuotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_error_component import (
            ApiV1PricingQuotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_reason_error_component import (
            ApiV1PricingQuotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_criticality_error_component import (
            ApiV1PricingQuotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_customer_email_error_component import (
            ApiV1PricingQuotesCreateCustomerEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_customer_name_error_component import (
            ApiV1PricingQuotesCreateCustomerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_debug_mode_error_component import (
            ApiV1PricingQuotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_display_name_error_component import (
            ApiV1PricingQuotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_kind_error_component import (
            ApiV1PricingQuotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_labels_error_component import (
            ApiV1PricingQuotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_name_error_component import (
            ApiV1PricingQuotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_non_field_errors_error_component import (
            ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_platform_service_error_component import (
            ApiV1PricingQuotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_error_component import (
            ApiV1PricingQuotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_id_error_component import (
            ApiV1PricingQuotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_reference_error_component import (
            ApiV1PricingQuotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_sla_availability_error_component import (
            ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_sla_target_error_component import (
            ApiV1PricingQuotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_slo_availability_error_component import (
            ApiV1PricingQuotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_slo_target_error_component import (
            ApiV1PricingQuotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_target_availability_error_component import (
            ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_tolerations_error_component import (
            ApiV1PricingQuotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_valid_until_error_component import (
            ApiV1PricingQuotesCreateValidUntilErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateCustomerNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateCustomerEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuotesCreateValidUntilErrorComponent):
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
        from ..models.api_v1_pricing_quotes_create_annotations_error_component import (
            ApiV1PricingQuotesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_at_error_component import (
            ApiV1PricingQuotesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_error_component import (
            ApiV1PricingQuotesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_archived_reason_error_component import (
            ApiV1PricingQuotesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_criticality_error_component import (
            ApiV1PricingQuotesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_customer_email_error_component import (
            ApiV1PricingQuotesCreateCustomerEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_customer_name_error_component import (
            ApiV1PricingQuotesCreateCustomerNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_debug_mode_error_component import (
            ApiV1PricingQuotesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_display_name_error_component import (
            ApiV1PricingQuotesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_kind_error_component import (
            ApiV1PricingQuotesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_labels_error_component import (
            ApiV1PricingQuotesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_name_error_component import (
            ApiV1PricingQuotesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_non_field_errors_error_component import (
            ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_platform_service_error_component import (
            ApiV1PricingQuotesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_error_component import (
            ApiV1PricingQuotesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_id_error_component import (
            ApiV1PricingQuotesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_provider_reference_error_component import (
            ApiV1PricingQuotesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_sla_availability_error_component import (
            ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_sla_target_error_component import (
            ApiV1PricingQuotesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_slo_availability_error_component import (
            ApiV1PricingQuotesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_slo_target_error_component import (
            ApiV1PricingQuotesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_target_availability_error_component import (
            ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_tolerations_error_component import (
            ApiV1PricingQuotesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_total_price_error_component import (
            ApiV1PricingQuotesCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quotes_create_valid_until_error_component import (
            ApiV1PricingQuotesCreateValidUntilErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuotesCreateAnnotationsErrorComponent
                | ApiV1PricingQuotesCreateArchivedAtErrorComponent
                | ApiV1PricingQuotesCreateArchivedErrorComponent
                | ApiV1PricingQuotesCreateArchivedReasonErrorComponent
                | ApiV1PricingQuotesCreateCriticalityErrorComponent
                | ApiV1PricingQuotesCreateCustomerEmailErrorComponent
                | ApiV1PricingQuotesCreateCustomerNameErrorComponent
                | ApiV1PricingQuotesCreateDebugModeErrorComponent
                | ApiV1PricingQuotesCreateDisplayNameErrorComponent
                | ApiV1PricingQuotesCreateKindErrorComponent
                | ApiV1PricingQuotesCreateLabelsErrorComponent
                | ApiV1PricingQuotesCreateNameErrorComponent
                | ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuotesCreatePlatformServiceErrorComponent
                | ApiV1PricingQuotesCreateProviderErrorComponent
                | ApiV1PricingQuotesCreateProviderIdErrorComponent
                | ApiV1PricingQuotesCreateProviderReferenceErrorComponent
                | ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuotesCreateSlaTargetErrorComponent
                | ApiV1PricingQuotesCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuotesCreateSloTargetErrorComponent
                | ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuotesCreateTolerationsErrorComponent
                | ApiV1PricingQuotesCreateTotalPriceErrorComponent
                | ApiV1PricingQuotesCreateValidUntilErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_0 = (
                        ApiV1PricingQuotesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_1 = (
                        ApiV1PricingQuotesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_2 = (
                        ApiV1PricingQuotesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_3 = (
                        ApiV1PricingQuotesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_4 = (
                        ApiV1PricingQuotesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_5 = (
                        ApiV1PricingQuotesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_6 = (
                        ApiV1PricingQuotesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_7 = (
                        ApiV1PricingQuotesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_8 = (
                        ApiV1PricingQuotesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_9 = (
                        ApiV1PricingQuotesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_10 = (
                        ApiV1PricingQuotesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_11 = (
                        ApiV1PricingQuotesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_12 = (
                        ApiV1PricingQuotesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_13 = (
                        ApiV1PricingQuotesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_14 = (
                        ApiV1PricingQuotesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_15 = (
                        ApiV1PricingQuotesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_16 = (
                        ApiV1PricingQuotesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_17 = (
                        ApiV1PricingQuotesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_18 = (
                        ApiV1PricingQuotesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_19 = (
                        ApiV1PricingQuotesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_20 = (
                        ApiV1PricingQuotesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_21 = (
                        ApiV1PricingQuotesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_22 = (
                        ApiV1PricingQuotesCreateCustomerNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_23 = (
                        ApiV1PricingQuotesCreateCustomerEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quotes_create_error_type_24 = (
                        ApiV1PricingQuotesCreateValidUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quotes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quotes_create_error_type_25 = (
                    ApiV1PricingQuotesCreateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quotes_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quotes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quotes_create_validation_error.additional_properties = d
        return api_v1_pricing_quotes_create_validation_error

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
