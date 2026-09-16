from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_apps_create_annotations_error_component import (
        ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_archived_at_error_component import (
        ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_archived_error_component import (
        ApiV1PricingQuoteAppsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_archived_reason_error_component import (
        ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_catalogue_app_error_component import (
        ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_count_error_component import (
        ApiV1PricingQuoteAppsCreateCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_criticality_error_component import (
        ApiV1PricingQuoteAppsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_debug_mode_error_component import (
        ApiV1PricingQuoteAppsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_display_name_error_component import (
        ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_kind_error_component import (
        ApiV1PricingQuoteAppsCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_labels_error_component import (
        ApiV1PricingQuoteAppsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_name_error_component import (
        ApiV1PricingQuoteAppsCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_non_field_errors_error_component import (
        ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_platform_service_error_component import (
        ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_provider_error_component import (
        ApiV1PricingQuoteAppsCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_provider_id_error_component import (
        ApiV1PricingQuoteAppsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_provider_reference_error_component import (
        ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_quote_workspace_error_component import (
        ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_quoted_price_error_component import (
        ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_sla_availability_error_component import (
        ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_sla_target_error_component import (
        ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_slo_availability_error_component import (
        ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_slo_target_error_component import (
        ApiV1PricingQuoteAppsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_target_availability_error_component import (
        ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_create_tolerations_error_component import (
        ApiV1PricingQuoteAppsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteAppsCreateValidationError")


@_attrs_define
class ApiV1PricingQuoteAppsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent |
            ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent | ApiV1PricingQuoteAppsCreateArchivedErrorComponent |
            ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent | ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent
            | ApiV1PricingQuoteAppsCreateCountErrorComponent | ApiV1PricingQuoteAppsCreateCriticalityErrorComponent |
            ApiV1PricingQuoteAppsCreateDebugModeErrorComponent | ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent |
            ApiV1PricingQuoteAppsCreateKindErrorComponent | ApiV1PricingQuoteAppsCreateLabelsErrorComponent |
            ApiV1PricingQuoteAppsCreateNameErrorComponent | ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent | ApiV1PricingQuoteAppsCreateProviderErrorComponent |
            ApiV1PricingQuoteAppsCreateProviderIdErrorComponent | ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent
            | ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent | ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent
            | ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent | ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent |
            ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent | ApiV1PricingQuoteAppsCreateSloTargetErrorComponent |
            ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent
        | ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent
        | ApiV1PricingQuoteAppsCreateArchivedErrorComponent
        | ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent
        | ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent
        | ApiV1PricingQuoteAppsCreateCountErrorComponent
        | ApiV1PricingQuoteAppsCreateCriticalityErrorComponent
        | ApiV1PricingQuoteAppsCreateDebugModeErrorComponent
        | ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent
        | ApiV1PricingQuoteAppsCreateKindErrorComponent
        | ApiV1PricingQuoteAppsCreateLabelsErrorComponent
        | ApiV1PricingQuoteAppsCreateNameErrorComponent
        | ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent
        | ApiV1PricingQuoteAppsCreateProviderErrorComponent
        | ApiV1PricingQuoteAppsCreateProviderIdErrorComponent
        | ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent
        | ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent
        | ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent
        | ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent
        | ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsCreateSloTargetErrorComponent
        | ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_apps_create_annotations_error_component import (
            ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_at_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_reason_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_count_error_component import (
            ApiV1PricingQuoteAppsCreateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_criticality_error_component import (
            ApiV1PricingQuoteAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_debug_mode_error_component import (
            ApiV1PricingQuoteAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_display_name_error_component import (
            ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_kind_error_component import (
            ApiV1PricingQuoteAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_labels_error_component import (
            ApiV1PricingQuoteAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_name_error_component import (
            ApiV1PricingQuoteAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_platform_service_error_component import (
            ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_error_component import (
            ApiV1PricingQuoteAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_id_error_component import (
            ApiV1PricingQuoteAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_reference_error_component import (
            ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_sla_availability_error_component import (
            ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_sla_target_error_component import (
            ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_slo_availability_error_component import (
            ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_slo_target_error_component import (
            ApiV1PricingQuoteAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_target_availability_error_component import (
            ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_tolerations_error_component import (
            ApiV1PricingQuoteAppsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsCreateCountErrorComponent):
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
        from ..models.api_v1_pricing_quote_apps_create_annotations_error_component import (
            ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_at_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_archived_reason_error_component import (
            ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_count_error_component import (
            ApiV1PricingQuoteAppsCreateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_criticality_error_component import (
            ApiV1PricingQuoteAppsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_debug_mode_error_component import (
            ApiV1PricingQuoteAppsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_display_name_error_component import (
            ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_kind_error_component import (
            ApiV1PricingQuoteAppsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_labels_error_component import (
            ApiV1PricingQuoteAppsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_name_error_component import (
            ApiV1PricingQuoteAppsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_platform_service_error_component import (
            ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_error_component import (
            ApiV1PricingQuoteAppsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_id_error_component import (
            ApiV1PricingQuoteAppsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_provider_reference_error_component import (
            ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_quoted_price_error_component import (
            ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_sla_availability_error_component import (
            ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_sla_target_error_component import (
            ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_slo_availability_error_component import (
            ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_slo_target_error_component import (
            ApiV1PricingQuoteAppsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_target_availability_error_component import (
            ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_create_tolerations_error_component import (
            ApiV1PricingQuoteAppsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent
                | ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent
                | ApiV1PricingQuoteAppsCreateArchivedErrorComponent
                | ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent
                | ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent
                | ApiV1PricingQuoteAppsCreateCountErrorComponent
                | ApiV1PricingQuoteAppsCreateCriticalityErrorComponent
                | ApiV1PricingQuoteAppsCreateDebugModeErrorComponent
                | ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent
                | ApiV1PricingQuoteAppsCreateKindErrorComponent
                | ApiV1PricingQuoteAppsCreateLabelsErrorComponent
                | ApiV1PricingQuoteAppsCreateNameErrorComponent
                | ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent
                | ApiV1PricingQuoteAppsCreateProviderErrorComponent
                | ApiV1PricingQuoteAppsCreateProviderIdErrorComponent
                | ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent
                | ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent
                | ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent
                | ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent
                | ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsCreateSloTargetErrorComponent
                | ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_0 = (
                        ApiV1PricingQuoteAppsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_1 = (
                        ApiV1PricingQuoteAppsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_2 = (
                        ApiV1PricingQuoteAppsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_3 = (
                        ApiV1PricingQuoteAppsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_4 = (
                        ApiV1PricingQuoteAppsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_5 = (
                        ApiV1PricingQuoteAppsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_6 = (
                        ApiV1PricingQuoteAppsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_7 = (
                        ApiV1PricingQuoteAppsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_8 = (
                        ApiV1PricingQuoteAppsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_9 = (
                        ApiV1PricingQuoteAppsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_10 = (
                        ApiV1PricingQuoteAppsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_11 = (
                        ApiV1PricingQuoteAppsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_12 = (
                        ApiV1PricingQuoteAppsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_13 = (
                        ApiV1PricingQuoteAppsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_14 = (
                        ApiV1PricingQuoteAppsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_15 = (
                        ApiV1PricingQuoteAppsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_16 = (
                        ApiV1PricingQuoteAppsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_17 = (
                        ApiV1PricingQuoteAppsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_18 = (
                        ApiV1PricingQuoteAppsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_19 = (
                        ApiV1PricingQuoteAppsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_20 = (
                        ApiV1PricingQuoteAppsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_21 = (
                        ApiV1PricingQuoteAppsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_22 = (
                        ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_23 = (
                        ApiV1PricingQuoteAppsCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_create_error_type_24 = (
                        ApiV1PricingQuoteAppsCreateCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_apps_create_error_type_25 = (
                    ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_apps_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_apps_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_apps_create_validation_error.additional_properties = d
        return api_v1_pricing_quote_apps_create_validation_error

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
