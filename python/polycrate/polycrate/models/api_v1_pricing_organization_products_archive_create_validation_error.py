from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_archive_create_active_from_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_active_until_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_reason_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_annotations_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_archived_at_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_archived_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_archived_reason_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_auto_managed_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_catalogue_app_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_content_type_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_criticality_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_debug_mode_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_display_name_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_internal_note_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_kind_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_labels_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_name_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_non_field_errors_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_object_id_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_platform_service_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_provider_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_provider_id_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_provider_reference_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_sla_availability_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_sla_target_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_slo_availability_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_slo_target_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_target_availability_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_archive_create_tolerations_error_component import (
        ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_archive_create_active_from_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_active_until_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_annotations_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_at_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_content_type_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_criticality_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_display_name_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_kind_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_labels_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_name_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_object_id_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_platform_service_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_id_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_sla_target_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_slo_target_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_target_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_tolerations_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent
            ):
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
        from ..models.api_v1_pricing_organization_products_archive_create_active_from_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_active_until_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_annotations_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_at_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_content_type_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_criticality_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_display_name_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_internal_note_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_kind_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_labels_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_name_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_object_id_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_platform_service_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_id_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_sla_target_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_slo_target_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_target_availability_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_archive_create_tolerations_error_component import (
            ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_0 = (
                        ApiV1PricingOrganizationProductsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_1 = (
                        ApiV1PricingOrganizationProductsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_2 = (
                        ApiV1PricingOrganizationProductsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_3 = (
                        ApiV1PricingOrganizationProductsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_4 = (
                        ApiV1PricingOrganizationProductsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_5 = (
                        ApiV1PricingOrganizationProductsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_6 = (
                        ApiV1PricingOrganizationProductsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_7 = (
                        ApiV1PricingOrganizationProductsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_8 = (
                        ApiV1PricingOrganizationProductsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_9 = (
                        ApiV1PricingOrganizationProductsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_10 = (
                        ApiV1PricingOrganizationProductsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_11 = (
                        ApiV1PricingOrganizationProductsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_12 = (
                        ApiV1PricingOrganizationProductsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_13 = (
                        ApiV1PricingOrganizationProductsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_14 = (
                        ApiV1PricingOrganizationProductsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_15 = (
                        ApiV1PricingOrganizationProductsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_16 = (
                        ApiV1PricingOrganizationProductsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_17 = (
                        ApiV1PricingOrganizationProductsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_18 = (
                        ApiV1PricingOrganizationProductsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_19 = (
                        ApiV1PricingOrganizationProductsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_20 = (
                        ApiV1PricingOrganizationProductsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_21 = (
                        ApiV1PricingOrganizationProductsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_22 = (
                        ApiV1PricingOrganizationProductsArchiveCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_23 = (
                        ApiV1PricingOrganizationProductsArchiveCreateContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_24 = (
                        ApiV1PricingOrganizationProductsArchiveCreateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_25 = (
                        ApiV1PricingOrganizationProductsArchiveCreateAutoManagedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_26 = (
                        ApiV1PricingOrganizationProductsArchiveCreateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_27 = (
                        ApiV1PricingOrganizationProductsArchiveCreateActiveUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_28 = (
                        ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_29 = (
                        ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_30 = (
                    ApiV1PricingOrganizationProductsArchiveCreateInternalNoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_archive_create_validation_error

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
