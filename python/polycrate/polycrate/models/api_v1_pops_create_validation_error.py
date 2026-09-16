from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_create_annotations_error_component import ApiV1PopsCreateAnnotationsErrorComponent
    from ..models.api_v1_pops_create_archived_at_error_component import ApiV1PopsCreateArchivedAtErrorComponent
    from ..models.api_v1_pops_create_archived_error_component import ApiV1PopsCreateArchivedErrorComponent
    from ..models.api_v1_pops_create_archived_reason_error_component import ApiV1PopsCreateArchivedReasonErrorComponent
    from ..models.api_v1_pops_create_city_error_component import ApiV1PopsCreateCityErrorComponent
    from ..models.api_v1_pops_create_country_error_component import ApiV1PopsCreateCountryErrorComponent
    from ..models.api_v1_pops_create_criticality_error_component import ApiV1PopsCreateCriticalityErrorComponent
    from ..models.api_v1_pops_create_debug_mode_error_component import ApiV1PopsCreateDebugModeErrorComponent
    from ..models.api_v1_pops_create_description_error_component import ApiV1PopsCreateDescriptionErrorComponent
    from ..models.api_v1_pops_create_display_name_error_component import ApiV1PopsCreateDisplayNameErrorComponent
    from ..models.api_v1_pops_create_kind_error_component import ApiV1PopsCreateKindErrorComponent
    from ..models.api_v1_pops_create_labels_error_component import ApiV1PopsCreateLabelsErrorComponent
    from ..models.api_v1_pops_create_latitude_error_component import ApiV1PopsCreateLatitudeErrorComponent
    from ..models.api_v1_pops_create_longitude_error_component import ApiV1PopsCreateLongitudeErrorComponent
    from ..models.api_v1_pops_create_name_error_component import ApiV1PopsCreateNameErrorComponent
    from ..models.api_v1_pops_create_non_field_errors_error_component import ApiV1PopsCreateNonFieldErrorsErrorComponent
    from ..models.api_v1_pops_create_platform_service_error_component import (
        ApiV1PopsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_create_pop_endpoint_remote_address_error_component import (
        ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_create_provider_entity_id_error_component import (
        ApiV1PopsCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_create_provider_error_component import ApiV1PopsCreateProviderErrorComponent
    from ..models.api_v1_pops_create_provider_id_error_component import ApiV1PopsCreateProviderIdErrorComponent
    from ..models.api_v1_pops_create_provider_reference_error_component import (
        ApiV1PopsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_create_reconciliation_enabled_error_component import (
        ApiV1PopsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_create_region_error_component import ApiV1PopsCreateRegionErrorComponent
    from ..models.api_v1_pops_create_sla_availability_error_component import (
        ApiV1PopsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_create_sla_target_error_component import ApiV1PopsCreateSlaTargetErrorComponent
    from ..models.api_v1_pops_create_slo_availability_error_component import (
        ApiV1PopsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_create_slo_target_error_component import ApiV1PopsCreateSloTargetErrorComponent
    from ..models.api_v1_pops_create_target_availability_error_component import (
        ApiV1PopsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_create_tolerations_error_component import ApiV1PopsCreateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1PopsCreateValidationError")


@_attrs_define
class ApiV1PopsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsCreateAnnotationsErrorComponent | ApiV1PopsCreateArchivedAtErrorComponent |
            ApiV1PopsCreateArchivedErrorComponent | ApiV1PopsCreateArchivedReasonErrorComponent |
            ApiV1PopsCreateCityErrorComponent | ApiV1PopsCreateCountryErrorComponent |
            ApiV1PopsCreateCriticalityErrorComponent | ApiV1PopsCreateDebugModeErrorComponent |
            ApiV1PopsCreateDescriptionErrorComponent | ApiV1PopsCreateDisplayNameErrorComponent |
            ApiV1PopsCreateKindErrorComponent | ApiV1PopsCreateLabelsErrorComponent | ApiV1PopsCreateLatitudeErrorComponent
            | ApiV1PopsCreateLongitudeErrorComponent | ApiV1PopsCreateNameErrorComponent |
            ApiV1PopsCreateNonFieldErrorsErrorComponent | ApiV1PopsCreatePlatformServiceErrorComponent |
            ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent | ApiV1PopsCreateProviderEntityIdErrorComponent |
            ApiV1PopsCreateProviderErrorComponent | ApiV1PopsCreateProviderIdErrorComponent |
            ApiV1PopsCreateProviderReferenceErrorComponent | ApiV1PopsCreateReconciliationEnabledErrorComponent |
            ApiV1PopsCreateRegionErrorComponent | ApiV1PopsCreateSlaAvailabilityErrorComponent |
            ApiV1PopsCreateSlaTargetErrorComponent | ApiV1PopsCreateSloAvailabilityErrorComponent |
            ApiV1PopsCreateSloTargetErrorComponent | ApiV1PopsCreateTargetAvailabilityErrorComponent |
            ApiV1PopsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsCreateAnnotationsErrorComponent
        | ApiV1PopsCreateArchivedAtErrorComponent
        | ApiV1PopsCreateArchivedErrorComponent
        | ApiV1PopsCreateArchivedReasonErrorComponent
        | ApiV1PopsCreateCityErrorComponent
        | ApiV1PopsCreateCountryErrorComponent
        | ApiV1PopsCreateCriticalityErrorComponent
        | ApiV1PopsCreateDebugModeErrorComponent
        | ApiV1PopsCreateDescriptionErrorComponent
        | ApiV1PopsCreateDisplayNameErrorComponent
        | ApiV1PopsCreateKindErrorComponent
        | ApiV1PopsCreateLabelsErrorComponent
        | ApiV1PopsCreateLatitudeErrorComponent
        | ApiV1PopsCreateLongitudeErrorComponent
        | ApiV1PopsCreateNameErrorComponent
        | ApiV1PopsCreateNonFieldErrorsErrorComponent
        | ApiV1PopsCreatePlatformServiceErrorComponent
        | ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsCreateProviderEntityIdErrorComponent
        | ApiV1PopsCreateProviderErrorComponent
        | ApiV1PopsCreateProviderIdErrorComponent
        | ApiV1PopsCreateProviderReferenceErrorComponent
        | ApiV1PopsCreateReconciliationEnabledErrorComponent
        | ApiV1PopsCreateRegionErrorComponent
        | ApiV1PopsCreateSlaAvailabilityErrorComponent
        | ApiV1PopsCreateSlaTargetErrorComponent
        | ApiV1PopsCreateSloAvailabilityErrorComponent
        | ApiV1PopsCreateSloTargetErrorComponent
        | ApiV1PopsCreateTargetAvailabilityErrorComponent
        | ApiV1PopsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_create_annotations_error_component import (
            ApiV1PopsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_at_error_component import (
            ApiV1PopsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_error_component import (
            ApiV1PopsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_reason_error_component import (
            ApiV1PopsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_city_error_component import ApiV1PopsCreateCityErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_country_error_component import (
            ApiV1PopsCreateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_criticality_error_component import (
            ApiV1PopsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_debug_mode_error_component import (
            ApiV1PopsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_description_error_component import (
            ApiV1PopsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_display_name_error_component import (
            ApiV1PopsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_kind_error_component import ApiV1PopsCreateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_labels_error_component import (
            ApiV1PopsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_latitude_error_component import (
            ApiV1PopsCreateLatitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_longitude_error_component import (
            ApiV1PopsCreateLongitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_name_error_component import ApiV1PopsCreateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_non_field_errors_error_component import (
            ApiV1PopsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_platform_service_error_component import (
            ApiV1PopsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_entity_id_error_component import (
            ApiV1PopsCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_error_component import (
            ApiV1PopsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_id_error_component import (
            ApiV1PopsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_reference_error_component import (
            ApiV1PopsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_reconciliation_enabled_error_component import (
            ApiV1PopsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_region_error_component import (
            ApiV1PopsCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_sla_availability_error_component import (
            ApiV1PopsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_sla_target_error_component import (
            ApiV1PopsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_slo_availability_error_component import (
            ApiV1PopsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_slo_target_error_component import (
            ApiV1PopsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_target_availability_error_component import (
            ApiV1PopsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_tolerations_error_component import (
            ApiV1PopsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsCreateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_create_annotations_error_component import (
            ApiV1PopsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_at_error_component import (
            ApiV1PopsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_error_component import (
            ApiV1PopsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_archived_reason_error_component import (
            ApiV1PopsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_city_error_component import ApiV1PopsCreateCityErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_country_error_component import (
            ApiV1PopsCreateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_criticality_error_component import (
            ApiV1PopsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_debug_mode_error_component import (
            ApiV1PopsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_description_error_component import (
            ApiV1PopsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_display_name_error_component import (
            ApiV1PopsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_kind_error_component import ApiV1PopsCreateKindErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_labels_error_component import (
            ApiV1PopsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_latitude_error_component import (
            ApiV1PopsCreateLatitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_longitude_error_component import (
            ApiV1PopsCreateLongitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_name_error_component import ApiV1PopsCreateNameErrorComponent  # noqa: PLC0415
        from ..models.api_v1_pops_create_non_field_errors_error_component import (
            ApiV1PopsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_platform_service_error_component import (
            ApiV1PopsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_pop_endpoint_remote_address_error_component import (
            ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_entity_id_error_component import (
            ApiV1PopsCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_error_component import (
            ApiV1PopsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_id_error_component import (
            ApiV1PopsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_provider_reference_error_component import (
            ApiV1PopsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_reconciliation_enabled_error_component import (
            ApiV1PopsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_region_error_component import (
            ApiV1PopsCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_sla_availability_error_component import (
            ApiV1PopsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_sla_target_error_component import (
            ApiV1PopsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_slo_availability_error_component import (
            ApiV1PopsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_slo_target_error_component import (
            ApiV1PopsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_target_availability_error_component import (
            ApiV1PopsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_create_tolerations_error_component import (
            ApiV1PopsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsCreateAnnotationsErrorComponent
                | ApiV1PopsCreateArchivedAtErrorComponent
                | ApiV1PopsCreateArchivedErrorComponent
                | ApiV1PopsCreateArchivedReasonErrorComponent
                | ApiV1PopsCreateCityErrorComponent
                | ApiV1PopsCreateCountryErrorComponent
                | ApiV1PopsCreateCriticalityErrorComponent
                | ApiV1PopsCreateDebugModeErrorComponent
                | ApiV1PopsCreateDescriptionErrorComponent
                | ApiV1PopsCreateDisplayNameErrorComponent
                | ApiV1PopsCreateKindErrorComponent
                | ApiV1PopsCreateLabelsErrorComponent
                | ApiV1PopsCreateLatitudeErrorComponent
                | ApiV1PopsCreateLongitudeErrorComponent
                | ApiV1PopsCreateNameErrorComponent
                | ApiV1PopsCreateNonFieldErrorsErrorComponent
                | ApiV1PopsCreatePlatformServiceErrorComponent
                | ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsCreateProviderEntityIdErrorComponent
                | ApiV1PopsCreateProviderErrorComponent
                | ApiV1PopsCreateProviderIdErrorComponent
                | ApiV1PopsCreateProviderReferenceErrorComponent
                | ApiV1PopsCreateReconciliationEnabledErrorComponent
                | ApiV1PopsCreateRegionErrorComponent
                | ApiV1PopsCreateSlaAvailabilityErrorComponent
                | ApiV1PopsCreateSlaTargetErrorComponent
                | ApiV1PopsCreateSloAvailabilityErrorComponent
                | ApiV1PopsCreateSloTargetErrorComponent
                | ApiV1PopsCreateTargetAvailabilityErrorComponent
                | ApiV1PopsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_0 = (
                        ApiV1PopsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_1 = ApiV1PopsCreateNameErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_2 = (
                        ApiV1PopsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_3 = ApiV1PopsCreateLabelsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_4 = (
                        ApiV1PopsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_5 = (
                        ApiV1PopsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_6 = ApiV1PopsCreateProviderErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_7 = (
                        ApiV1PopsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_8 = (
                        ApiV1PopsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_9 = (
                        ApiV1PopsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_10 = (
                        ApiV1PopsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_11 = ApiV1PopsCreateKindErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_12 = (
                        ApiV1PopsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_13 = (
                        ApiV1PopsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_14 = (
                        ApiV1PopsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_15 = (
                        ApiV1PopsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_16 = (
                        ApiV1PopsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_17 = (
                        ApiV1PopsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_18 = (
                        ApiV1PopsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_19 = (
                        ApiV1PopsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_20 = (
                        ApiV1PopsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_21 = (
                        ApiV1PopsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_22 = ApiV1PopsCreateRegionErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_23 = ApiV1PopsCreateCountryErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_24 = ApiV1PopsCreateCityErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_pops_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_25 = (
                        ApiV1PopsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_26 = (
                        ApiV1PopsCreateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_27 = (
                        ApiV1PopsCreateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_create_error_type_28 = (
                        ApiV1PopsCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_create_error_type_29 = (
                    ApiV1PopsCreatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_create_validation_error.additional_properties = d
        return api_v1_pops_create_validation_error

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
