from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_create_active_from_error_component import (
        ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_active_until_error_component import (
        ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_agreed_price_error_component import (
        ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_agreed_price_reason_error_component import (
        ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_annotations_error_component import (
        ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_archived_at_error_component import (
        ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_archived_error_component import (
        ApiV1PricingOrganizationProductsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_archived_reason_error_component import (
        ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_auto_managed_error_component import (
        ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_catalogue_app_error_component import (
        ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_content_type_error_component import (
        ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_criticality_error_component import (
        ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_debug_mode_error_component import (
        ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_display_name_error_component import (
        ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_internal_note_error_component import (
        ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_kind_error_component import (
        ApiV1PricingOrganizationProductsCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_labels_error_component import (
        ApiV1PricingOrganizationProductsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_name_error_component import (
        ApiV1PricingOrganizationProductsCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_non_field_errors_error_component import (
        ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_object_id_error_component import (
        ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_platform_service_error_component import (
        ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_provider_error_component import (
        ApiV1PricingOrganizationProductsCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_provider_id_error_component import (
        ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_provider_reference_error_component import (
        ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_reconciliation_enabled_error_component import (
        ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_sla_availability_error_component import (
        ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_sla_target_error_component import (
        ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_slo_availability_error_component import (
        ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_slo_target_error_component import (
        ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_target_availability_error_component import (
        ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_create_tolerations_error_component import (
        ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsCreateValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent |
            ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent |
            ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent |
            ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent |
            ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent |
            ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent |
            ApiV1PricingOrganizationProductsCreateArchivedErrorComponent |
            ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent |
            ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent |
            ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent |
            ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent |
            ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent |
            ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent |
            ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent |
            ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent |
            ApiV1PricingOrganizationProductsCreateKindErrorComponent |
            ApiV1PricingOrganizationProductsCreateLabelsErrorComponent |
            ApiV1PricingOrganizationProductsCreateNameErrorComponent |
            ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent |
            ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent |
            ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent |
            ApiV1PricingOrganizationProductsCreateProviderErrorComponent |
            ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent |
            ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent |
            ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent |
            ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent |
            ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent |
            ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent
        | ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent
        | ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent
        | ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent
        | ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent
        | ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent
        | ApiV1PricingOrganizationProductsCreateArchivedErrorComponent
        | ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent
        | ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent
        | ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent
        | ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent
        | ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent
        | ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent
        | ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent
        | ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent
        | ApiV1PricingOrganizationProductsCreateKindErrorComponent
        | ApiV1PricingOrganizationProductsCreateLabelsErrorComponent
        | ApiV1PricingOrganizationProductsCreateNameErrorComponent
        | ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent
        | ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent
        | ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent
        | ApiV1PricingOrganizationProductsCreateProviderErrorComponent
        | ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent
        | ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent
        | ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent
        | ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent
        | ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent
        | ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_create_active_from_error_component import (
            ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_active_until_error_component import (
            ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_annotations_error_component import (
            ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_at_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_content_type_error_component import (
            ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_criticality_error_component import (
            ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_display_name_error_component import (
            ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_kind_error_component import (
            ApiV1PricingOrganizationProductsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_labels_error_component import (
            ApiV1PricingOrganizationProductsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_name_error_component import (
            ApiV1PricingOrganizationProductsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_object_id_error_component import (
            ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_platform_service_error_component import (
            ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_id_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_sla_target_error_component import (
            ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_slo_target_error_component import (
            ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_target_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_tolerations_error_component import (
            ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent):
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
        from ..models.api_v1_pricing_organization_products_create_active_from_error_component import (
            ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_active_until_error_component import (
            ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_annotations_error_component import (
            ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_at_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_content_type_error_component import (
            ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_criticality_error_component import (
            ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_display_name_error_component import (
            ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_internal_note_error_component import (
            ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_kind_error_component import (
            ApiV1PricingOrganizationProductsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_labels_error_component import (
            ApiV1PricingOrganizationProductsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_name_error_component import (
            ApiV1PricingOrganizationProductsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_object_id_error_component import (
            ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_platform_service_error_component import (
            ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_id_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_sla_target_error_component import (
            ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_slo_target_error_component import (
            ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_target_availability_error_component import (
            ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_create_tolerations_error_component import (
            ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent
                | ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent
                | ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent
                | ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent
                | ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent
                | ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent
                | ApiV1PricingOrganizationProductsCreateArchivedErrorComponent
                | ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent
                | ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent
                | ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent
                | ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent
                | ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent
                | ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent
                | ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent
                | ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent
                | ApiV1PricingOrganizationProductsCreateKindErrorComponent
                | ApiV1PricingOrganizationProductsCreateLabelsErrorComponent
                | ApiV1PricingOrganizationProductsCreateNameErrorComponent
                | ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent
                | ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent
                | ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent
                | ApiV1PricingOrganizationProductsCreateProviderErrorComponent
                | ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent
                | ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent
                | ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent
                | ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent
                | ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent
                | ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_0 = (
                        ApiV1PricingOrganizationProductsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_1 = (
                        ApiV1PricingOrganizationProductsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_2 = (
                        ApiV1PricingOrganizationProductsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_3 = (
                        ApiV1PricingOrganizationProductsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_4 = (
                        ApiV1PricingOrganizationProductsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_5 = (
                        ApiV1PricingOrganizationProductsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_6 = (
                        ApiV1PricingOrganizationProductsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_7 = (
                        ApiV1PricingOrganizationProductsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_8 = (
                        ApiV1PricingOrganizationProductsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_9 = (
                        ApiV1PricingOrganizationProductsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_10 = (
                        ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_11 = (
                        ApiV1PricingOrganizationProductsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_12 = (
                        ApiV1PricingOrganizationProductsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_13 = (
                        ApiV1PricingOrganizationProductsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_14 = (
                        ApiV1PricingOrganizationProductsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_15 = (
                        ApiV1PricingOrganizationProductsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_16 = (
                        ApiV1PricingOrganizationProductsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_17 = (
                        ApiV1PricingOrganizationProductsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_18 = (
                        ApiV1PricingOrganizationProductsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_19 = (
                        ApiV1PricingOrganizationProductsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_20 = (
                        ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_21 = (
                        ApiV1PricingOrganizationProductsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_22 = (
                        ApiV1PricingOrganizationProductsCreateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_23 = (
                        ApiV1PricingOrganizationProductsCreateContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_24 = (
                        ApiV1PricingOrganizationProductsCreateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_25 = (
                        ApiV1PricingOrganizationProductsCreateAutoManagedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_26 = (
                        ApiV1PricingOrganizationProductsCreateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_27 = (
                        ApiV1PricingOrganizationProductsCreateActiveUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_28 = (
                        ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_create_error_type_29 = (
                        ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_create_error_type_30 = (
                    ApiV1PricingOrganizationProductsCreateInternalNoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_create_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_create_validation_error

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
