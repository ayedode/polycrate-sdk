from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_apps_archive_create_annotations_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_archived_at_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_archived_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_archived_reason_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_catalogue_app_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_count_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_criticality_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_debug_mode_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_display_name_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_kind_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_labels_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_name_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_non_field_errors_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_platform_service_error_component import (
        ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_provider_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_provider_id_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_provider_reference_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_quote_workspace_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_quoted_price_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_sla_availability_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_sla_target_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_slo_availability_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_slo_target_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_target_availability_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_apps_archive_create_tolerations_error_component import (
        ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteAppsArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingQuoteAppsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent | ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_apps_archive_create_annotations_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_at_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_reason_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_count_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_criticality_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_debug_mode_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_display_name_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_kind_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_labels_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_name_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_platform_service_error_component import (
            ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_id_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_reference_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_sla_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_sla_target_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_slo_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_slo_target_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_target_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_tolerations_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent):
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
        from ..models.api_v1_pricing_quote_apps_archive_create_annotations_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_at_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_archived_reason_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_catalogue_app_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_count_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_criticality_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_debug_mode_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_display_name_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_kind_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_labels_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_name_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_platform_service_error_component import (
            ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_id_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_provider_reference_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_quote_workspace_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_quoted_price_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_sla_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_sla_target_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_slo_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_slo_target_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_target_availability_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_apps_archive_create_tolerations_error_component import (
            ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_0 = (
                        ApiV1PricingQuoteAppsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_1 = (
                        ApiV1PricingQuoteAppsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_2 = (
                        ApiV1PricingQuoteAppsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_3 = (
                        ApiV1PricingQuoteAppsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_4 = (
                        ApiV1PricingQuoteAppsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_5 = (
                        ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_6 = (
                        ApiV1PricingQuoteAppsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_7 = (
                        ApiV1PricingQuoteAppsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_8 = (
                        ApiV1PricingQuoteAppsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_9 = (
                        ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_10 = (
                        ApiV1PricingQuoteAppsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_11 = (
                        ApiV1PricingQuoteAppsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_12 = (
                        ApiV1PricingQuoteAppsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_13 = (
                        ApiV1PricingQuoteAppsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_14 = (
                        ApiV1PricingQuoteAppsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_15 = (
                        ApiV1PricingQuoteAppsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_16 = (
                        ApiV1PricingQuoteAppsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_17 = (
                        ApiV1PricingQuoteAppsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_18 = (
                        ApiV1PricingQuoteAppsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_19 = (
                        ApiV1PricingQuoteAppsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_20 = (
                        ApiV1PricingQuoteAppsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_21 = (
                        ApiV1PricingQuoteAppsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_22 = (
                        ApiV1PricingQuoteAppsArchiveCreateQuoteWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_23 = (
                        ApiV1PricingQuoteAppsArchiveCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_24 = (
                        ApiV1PricingQuoteAppsArchiveCreateCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_25 = (
                    ApiV1PricingQuoteAppsArchiveCreateQuotedPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_apps_archive_create_error_type_25

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_apps_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_apps_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_quote_apps_archive_create_validation_error

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
